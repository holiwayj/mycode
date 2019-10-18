#!/usr/bin/env python3
ipchk = input("Apply an IP address: ")
if ipchk == "192.168.70.1":
    print("Looks like the IP address was set: " + ipchk + " This is not reccomended")
elif ipchk:
    print("Looks like the IP addres was set: " + ipchk)
else:
    print("You did not provide input.")

