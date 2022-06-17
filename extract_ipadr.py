#!/usr/bin/python3
import re
string = f'''Address         Age        HardwareAddr   State      Type  Interface
10.4.9.2        00:35:55   0030.7131.abfc  Dynamic    ARPA  MgmtEth0/RP1/CPU0/0
10.4.9.1        00:35:55   0000.0c07.ac24  Dynamic    ARPA  MgmtEth0/RP1/CPU0/0
10.4.9.99       00:49:12   0007.ebea.44d0  Dynamic    ARPA  MgmtEth0/RP1/CPU0/0
10.4.9.199      -          0001.c9eb.dffe  Interface  ARPA  MgmtEth0/RP1/CPU0/0'''

'''compare = "10.\d{1}.\d{1}.\d{1,3}"
output = re.findall(compare,string)
#print(output)'''

list1 = []
split_line = string.split("\n")
print(split_line)

for line in split_line:
    word = line.split()
    list1.append(word)
print(list1)

[['Address', 'Age', 'Hardware', 'Addr', 'State', 'Type', 'Interface'], ['10.4.9.2', '00:35:55', '0030.7131.abfc', 'Dynamic', 'ARPA', 'MgmtEth0/RP1/CPU0/0'], ['10.4.9.1', '00:35:55', '0000.0c07.ac24', 'Dynamic', 'ARPA', 'MgmtEth0/RP1/CPU0/0'], ['10.4.9.99', '00:49:12', '0007.ebea.44d0', 'Dynamic', 'ARPA', 'MgmtEth0/RP1/CPU0/0'], ['10.4.9.199', '-', '0001.c9eb.dffe', 'Interface', 'ARPA', 'MgmtEth0/RP1/CPU0/0']]

ipadr = input("enter ip address")
for lines in list1:
    #print(lines)
    for word in lines:
        #print(word)
        if ipadr == word:
            print(lines[2])
