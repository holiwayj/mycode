#!/usr/bin/env python3
dns_file = open("dnsservers.txt")
dnslist = dns_file.readlines()
for svr in dnslist:
    print(svr, end = "")
    dns_file.close()

