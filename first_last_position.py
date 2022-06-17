#!/usr/bin/python3
nums = [5,7,7,8,8,10,8]
target = 8
element_list = []
for index, element in enumerate(nums):
    if element == target:
        i = (index, element)
        element_list.append(i)
        print(element_list)
print("first position, last position", element_list[0], element_list[-1])

