from scapy.all import ARP, Ether, srp

#Define my network (replace with my subnet)
network = ""

def scan_network(ip_range):
    # create ARP request pack
    arp-request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    # send packet and recieve responses
    result = srp(packet, timeout=2, verbose=False)[0]

    # print discovered devices
    print("Devices found on network:")
    for sent, recieved in result:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

scan_network(network)
