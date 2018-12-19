#!/usr/bin/python

# Using argparse python3
import scapy.all as scapy
import optparse

# Active from terminal
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="target to scan for its ip & MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an target, use --help for more info.")
    return options


# Scanning network
def scan(ip):
    # Creating instance of scapy ARP
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n----------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_results = scan(options.target)
print_result(scan_results)
