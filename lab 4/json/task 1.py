import json

file_path = r'C:\Users\Админ\Desktop\pp2 labs\lab 4\json\sample-data.json'
with open(file_path, 'r') as file:
    data = json.load(file)

interfaces = data.get('imdata', [])

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface.get('fabricEthEstcEp', {}).get('attributes', {}).get('dn', '')
    description = interface.get('fabricEthEstcEp', {}).get('attributes', {}).get('descr', 'inherit')
    speed = interface.get('fabricEthEstcEp', {}).get('attributes', {}).get('speed', 'inherit')
    mtu = interface.get('fabricEthEstcEp', {}).get('attributes', {}).get('mtu', 'inherit')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
