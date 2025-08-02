import json
import urllib.request
import os

url = os.getenv("ENDPOINTS_URL", "https://raw.githubusercontent.com/ircfspace/endpoint/refs/heads/main/ip.json")
output_file = os.getenv("OUTPUT_FILE", "result.json")

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

ipv4_list = data.get("ipv4", [])
ipv6_list = data.get("ipv6", [])

public_entries = [
    "warp,;,gool=true&scan=true#WARP | GOOL+SCAN",
    "warp,;,cfon=true&scan=true#WARP | CFON RANDOM"
]

for ip in ipv4_list:
    ip = ip.strip()
    if ip:
        public_entries.append(f"warp,;,endpoint={ip}#WARP | {ip}")

for ip in ipv6_list:
    ip = ip.strip()
    if ip:
        public_entries.append(f"warp,;,endpoint={ip}#WARP | {ip}")

output = {
    "PUBLIC": public_entries,
    "other": [],
    "IRANCELL": [],
    "PISHGAMAN": [],
    "TCI": [],
    "MCI": [],
    "SHATEL": [],
    "PARSONLINE": [],
    "RIGHTEL": []
}

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4, ensure_ascii=False)
