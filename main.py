import requests
import socket
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
h1 = input("Enter your hackerone username: ")
target_ip = input("Enter IP or domain: ")
header = {f"X-HackerOne-Research": h1}
open_http_ports = []

# Use a global session for connection reuse (faster)
session = requests.Session()
session.headers.update(header)

# Scan function
def scan_port(port):
    url = f"http://{target_ip}:{port}/"
    try:
        response = session.get(url, timeout=0.3)
        if response.status_code in [200, 204, 301, 302, 307, 401, 403]:
            return port, response.status_code
    except (requests.exceptions.RequestException, socket.gaierror):
        pass
    return None, None

# Port range
ports = list(range(1, 65536))

# Progress bar + thread pool
with ThreadPoolExecutor(max_workers=30) as executor:
    results = list(tqdm(executor.map(scan_port, ports), total=len(ports), desc="Scanning Ports"))

# Process results
for port, status in results:
    if port:
        print(f"Port {port} responded with status code: {status}")
        open_http_ports.append(port)

# Final summary
print(f"\nTotal open HTTP ports with the header: {len(open_http_ports)}")
print(f"Open HTTP ports: {open_http_ports}")
