#!/usr/bin/python3
import re

with open("show_interfaces.txt","r") as file:
    txt = list(map(list, file.read().splitlines()))
#print(txt)

int_dict = {}
values_list = []
for index, line in enumerate(txt):
    temp = "".join(line)
    interface = re.match("GigabitEthernet\d+\/\d+", temp)
    if interface:
        word = temp.split()
        int_dict[word[0]] = {}
        #print(word)
        interface_name = word[0]
        #print(int_dict)
    if "address" in temp:
        #print(temp)
        addr_line = temp.split()
        #print(addr_line)
        for index,val in enumerate(addr_line):
            #print(val)
            if "address" == val:
                #print(type(addr_line[index+2]))
                int_dict[interface_name]["address"] = (addr_line[index+2])
                #print(int_dict)

    if "MTU" in temp:
        mtu_line = temp.split()
        #print(mtu_line)
        for index,mtu_val in enumerate(mtu_line):
            #print(val)
            if "MTU" == mtu_val:
                int_dict[interface_name]["MTU"] = mtu_line[index+1]
                #print(values_list)
    if "BW" in temp:
        bw_line = temp.split()
        #print(mtu_line)
        for index,bw_val in enumerate(bw_line):
            #print(val)
            if "BW" == bw_val:
                int_dict[interface_name]["BW"] = mtu_line[index+1]
print(int_dict)

