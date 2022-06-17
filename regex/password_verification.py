#!/usr/bin/python3
import re
string = "Nish#@a8j"
check = re.findall("((?=.*[A-Z]).*(?=.*[0-9]).*(?=.*@).*(?=.*#).{6,15})",string)
if check:
    print('match')
else:
    print('not matched')
    
