#!/usr/bin/python3
import re 
text = "aab_cbbb"
output = re.findall(r"[a-z]+_[a-z]+",text)
print(output)
