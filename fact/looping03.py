#!/usr/bin/env python3
'''
This is test code
'''
import uuid
HOWMANY = int(input("How many UUID's should be generated? "))
print("Generating UUIDs..... ")
for rando in range(HOWMANY):
    print(uuid.uuid4())
