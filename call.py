#!/usr/bin/python3

list1 = [2,1,3,2,2]

for index,val in enumerate(list1[:]):
    if val == 2:
        print(list1,index)
        del list1[index:index+2]
        print(list1,index)
