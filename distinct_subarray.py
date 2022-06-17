#!/usr/bin/python3

array = ["a","b","b","e","c","d"]
list2 = []
string  = ''
i = 0
nxt = 0
sublist = 3 
while i < len(array):
    print(i)
    if array[i] not in string:
        string += array[i]
        i += 1
        sublist -= 1
        #print(sublist, array[i], string)
        if sublist == 0:
            list2.append(string)
            print(list2)
            nxt += 1
            i = nxt
            string=''
            sublist=3
          #  print(i)
            continue

    else:
        string += array[i]
        i += 1

