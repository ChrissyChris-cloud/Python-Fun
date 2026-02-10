from scapy.all import sniff

# Function to process captured packets
def process_packet(packet):
    print(packet.summary())

# Start sniffing on default network interface
print("Starting network sniffer...")
sniff(prn=process_packet, count=10)  # Captures 10 packets
