#!/usr/bin/env python3
import csv
f = open("csv_users.txt", "r")
i = 0
for row in csv.reader(f):
    i = i + 1
    filename = "admin.rc%d"%(i,)
    rcfile = open(filename, "w")
    print("export OS_AUTH_URL" + row[0], file=rcfile)
    print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
    print("export OS_PROJECT_NAME" , file=rcfile)
    print("export OS_PROJECT_DOMAIN_NAME" , file=rcfile)
    print("export OS_USERNAME=", file=rcfile)
    print("export OS_USER_DOMAIN_NAME=", file=rcfile)
    print("export OS_PASSWORD=" , file=rcfile)
    rcfile.close()
