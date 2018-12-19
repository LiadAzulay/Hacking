#!/usr/bin/env python
import scapy.all as scapy


# Sniffing giving interface
def sniff(interface):
    scapy.sniff(iface=interface, store=process_sniffed_packet)


# Returning mac base on ip address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(pdst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def process_sniffed_packet(packet):
    if packet.haslayer[scapy.ARP] and packet[scapy.ARP].op == 2:
        # Getting the real mac
        real_mac = get_mac(packet[scapy.ARP].psrc)
        # Getting the mac from the response
        response_mac = packet[scapy.ARP].hwsrc
        # Compering between the two mac addresses
        if real_mac != response_mac:
            print("[+] You under attack!!")


sniff("eth0")
