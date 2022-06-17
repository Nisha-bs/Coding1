#!/usr/bin/python3
import re

input_string = "1.168.0.35 address 200.168.0.31"
output = re.findall("\d[0-9][0-9]{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", input_string)
print(output)

