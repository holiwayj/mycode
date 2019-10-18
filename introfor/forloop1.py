#!/usr/bin/env python3
vendors = ["Cisco", "Juniper", "big-ip", "F5", "Arista", "alta3", "zach", "stuart"]
approved_vendors = ["Cisco", "Juniper", "big-ip"]
for x in vendors:
    print("\nThe Vendor is: " + x, end=" ")
    if x not in approved_vendors:
        print("\nNOT IN APPROVED VENDORS", end=" ")
    print("\nOur loop has ended.")

