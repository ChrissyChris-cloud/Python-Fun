CloudDeploy[
    APIFunction[{"x" -> "Integer"}, #x^2 &]
]

import socket

def scan_ports(target, ports):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.settimeout(1)
         result = s.connect_ex((target, port))
         if result == 0:
             print(f"port {port} is open")
        s.close()

target_ip = "192.168.1.1" # Change to target IP
ports = range(20,100) # Scanning ports 20-100
acan_ports(target_ip, ports)

include <stdio.h>

void secret_function() {
    printf("You,ve accessed the secret function!\n");
}

int main() {
    printf("Try to reach the secret function!\n");
    return 0;
}

import os

def cleanup_tmp_files(directory):
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))
        print(f2Deleted {file}")

cleanup_tmp_files("/path/to/directory") # change to relevant directory path

