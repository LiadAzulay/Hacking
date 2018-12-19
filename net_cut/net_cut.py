import netfilterqueue as nf


# Only putting all packets in queue and not forwarding them
# Cutting all connections

def process_packet(packet):
    packet.drop()


queue = nf.NetfilterQueue()

queue.bind(0, process_packet)
queue.run()
