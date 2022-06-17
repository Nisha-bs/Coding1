#!/usr/bin/python3

list1 = [2,2,2]
iter_count =0
count = 0
while True:
    count=0
    for numbers in range(len(list1)):
        if list1[numbers] > numbers + 1:
            list1[numbers] -= 1
        elif list1[numbers] < numbers + 1:
            list1[numbers] += 1
        elif list1[numbers] == numbers + 1:
            count+=1
            continue
    if count == len(list1):
        break
    else:
        iter_count+=1

print(iter_count)

        

