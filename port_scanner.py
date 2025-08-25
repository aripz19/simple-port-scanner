import socket

# Simple Port Scanner
def scan_ports(target, ports):
    print(f"Scanning {target} ...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # timeout for connection
            result = sock.connect_ex((target, port))  # 0 = open, >0 = closed
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Example usage
if __name__ == "__main__":
    target = "127.0.0.1"  # localhost
    ports_to_scan = [21, 22, 80, 443, 3306]  # FTP, SSH, HTTP, HTTPS, MySQL
    scan_ports(target, ports_to_scan)
        
