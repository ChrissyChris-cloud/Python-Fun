import socket
from tqdm import tqdm  # Progress bar

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    open_ports = []

    for port in tqdm(ports, desc="Scanning ports"):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass  # Ignore errors for closed ports

    if open_ports:
        print(f"Open Ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target}")

# Example Usage
target_ip = ""  # Change to your target IP
port_range = range(1, 1024)  # Scans first 1024 ports
scan_ports(target_ip, port_range)
