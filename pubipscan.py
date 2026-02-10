import shodan

API_KEY = "YOUR_SHODAN_API_KEY"
shodan_api = shodan.Shodan(API_KEY)

ip = "8.8.8.8"  # Replace with a target public IP

try:
    result = shodan_api.host(ip)
    print(f"Scanning IP: {ip}")
    print(f"Open Ports: {result['ports']}")
    print(f"Organization: {result.get('org', 'N/A')}")
    print(f"Operating System: {result.get('os', 'N/A')}")
except shodan.APIError as e:
    print(f"Error: {e}")
