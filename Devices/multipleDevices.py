from random import choice 
import string
import tabulate #pip install tabulate as it is not a default package
from operator import itemgetter
from pprint import pprint

devices = list() #An empty list to store the devices
#devices = []

#For loop to create a large number of devices
for index in range(100):
    #devices are stored in a dictionary, hence
    device = dict()


    device["name"] = (
            choice(["r2", "r3", "r4", "r6", "r10"])
            + choice(["L", "U"])
            + choice(string.ascii_letters)
            )

#random vendor from choices: Juniper, Cisco, Huawei, Arista
device["vendor"] = choice(["cisco", "juniper", "Arista"])
if device["vendor"] == "cisco":
    device["os"] = choice(["nexus", "ios", "iosxe", "iosxr"])
    device["version"] = choice(["15.88x", "12.98(1).74", "20.45"])
elif device["vendor"] == "juniper":
    device["os"] = "junos"
    device["version"] = choice(["38.90", "6.03", "40.24.3"])
elif device["vendor"] == "Arista":
    device["os"] = "aos"
    device["version"] = choice(["34.90.1", "9.06", "78.53"])
device["ip"] = "10.0.0." + str(index)

print()
for key, value in device.items():
    print(f"{key:>16s}: {value}") 

#Add the device to the list
devices.append(device)
print(devices)


# Using tabulate to print devices
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))