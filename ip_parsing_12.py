#!/usr/bin/python3
import re
text = '''R1#show ip interface brief
Interface             IP-Address      OK? Method Status        Protocol
FastEthernet0/0       15.0.15.1       YES manual up            up
FastEthernet0/1       10.0.12.1       YES manual up            up
FastEthernet0/2       10.0.13.1       YES manual up            up
FastEthernet0/3       unassigned      YES unset  up            down
Loopback0             10.1.1.1        YES manual up            up
Loopback100           100.0.0.1       YES manual up            up'''

result = {}
text_split = text.split('\n')
for line in text_split:
    #print(line)
    line = line.split()
    print(line)
    if line[1][0].isdigit():
        print(line[1][0])
        inter, addr,status, *other = line
        result[inter] = [addr,status]
        print(result)
    else:
        continue

print(result)
