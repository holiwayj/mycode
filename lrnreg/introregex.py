#!/usr/bin/env python3
import urllib.request
import re
print("Where should we search? ")
url = input()
print("Great!, We will try to open this URL: " + str(url) + " to search for the phrase: ")
searchfor = input()
searchme = urllib.request.urlopen(url).read().decode("utf-8")
if re.search(searchfor, searchme):
    print("Found a match!")
else:
    print("No Match Found.")
