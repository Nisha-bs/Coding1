#!/usr/bin/python3
import re 
string = "4-4.00"
'''
-1.00
+4.54
'''
#check = re.findall("^[-+.]?\d+\.\d+$",string)

check = re.match(r"(\d+)[-+](\d+)\.(\d+)",string)
print(check.group(3))

