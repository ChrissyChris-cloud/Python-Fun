import socket

# define target
target = "172.166.156.100"
ports = [22, 80, 443, 3306] # common ports to check

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # set a timeoutfor the connection attempt
    result = sock.connect_ex((target, port)) # 0 means open, other values mean closed
    if result == 0:
        print(f"port {ports} is OPEN")
    else:
        print(f"port {port} is CLOSED")
    sock.close()
