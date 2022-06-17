#!/usr/bin/python3

strs = ["fiower","flow","fioght","fit"]
string = ""
nxt_string = ""
prefix_list = []
min_len = min(strs)
print(min_len)

for index in range(len(strs)-1):
    string = strs[index]
    nxt_string = strs[index+1]
    print("string , nxt_string",string, nxt_string)
    for ind in range(len(min_len)):
        prefix = string[:ind]
        nxt_prefix = string[:ind]
        print("prefix, nxt_prefix", prefix, nxt_prefix)
        if prefix == nxt_prefix:
            continue
        else:
            print(prefix)
            break
    else:
        break
    prefix_list.append(prefix[:len(prefix)-1])
    print(prefix[:len(prefix)-1], prefix_list)
'''prefix_min = min(prefix_list)
print(prefix_min)

for i in prefix_list:
    if prefix_min != i:
        break
    else:
        print(prefix_min)
'''
