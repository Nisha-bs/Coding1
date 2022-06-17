#!/usr/bin/python3

num1 = 0
num2 = 1
list1 = []

list1.append(num1)
list1.append(num2)

for num in range(10):
    result = list1[num] + list1[num+1]
    list1.append(result)
print(list1)
