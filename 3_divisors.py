#!/usr/bin/python3

query = 6

for i in range(1,query+1):
    count = 1
    list1 = []
    #while count != i+1:
    while count <= query:
        if i % count  == 0:
            list1.append(count)
        count += 1
    print(list1)
