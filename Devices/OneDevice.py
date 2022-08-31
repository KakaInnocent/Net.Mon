#This script shows one device in the system.
#That is a representation of one network device in the system.
from pprint import pprint 

device = {
        "name": "dxs-n8jv-ao",
        "vendor": "Cisco",
        "Model": "Nexus9000 C9300v Chassis",
        "os": "nxos",
        "version": "9.3(3)",
        "ip": "10.1.1.1",
        }
#Printing the output
#PRETTY PRINT
print("\n------------PRETTY PRINT-----------")
pprint(device)

#FORMATTED OUTPUT
print("\n----------USING F-STRING-------")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
