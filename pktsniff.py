from scapy.all import sniff

#function for processing
def packet_callback(packet):
    print(packet.summary())

#capture 5 packets from the network
sniff(prn=packet_callback, count=5)
