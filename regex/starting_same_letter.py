#!/usr/bin/python3
import re
words = ['python php','java jai']
for string in words:
    #match = re.match('(p\w+)\W(p\w+)',string)
    if match:
        print(match.groups(),match.span())
