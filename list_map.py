#!/usr/bin/python3

list1 = [7,6,2]
list1.sort()
print(list1)
#list1 = [2,6,7]
#list2 = [1,2,3]
list2 = []
list1_length = len(list1)
for ele in range(1, list1_length+1):
    list2.append(ele)
    list2.sort()
print(list2)

count = 0
while True:
    for element in range(len(list1)):
        if list1[element] > list2[element]:
            list1[element] -= 1
        elif list1[element] < list2[element]:
            list1[element] += 1
        elif list1[element] == list2[element]:
            continue
    count += 1
    if list1 == list2:
        break
print(count)
