from random import choice 
import string
from tabulate import tabulate #pip install tabulate as it is not a default package
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

