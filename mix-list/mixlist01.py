#!/usr/bin/env python3
jon_list = [ "192.164.0.5",5060, "UP" ]
print("The first line in this list (IP):" + jon_list[0])
print("The second line in this list (PORT):" + str(jon_list[1]))
print("The last line in this list (Status):" + jon_list[2])
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print("When I " + new_list[5] + " into IP addresses, " + new_list[3] + "or " + new_list[4] + ". I am unable to ping ports: " + str(new_list[0]) + "," + new_list[1] + ", or " + str(new_list[2]) + ".")
