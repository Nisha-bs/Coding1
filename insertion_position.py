#!/usr/bin/python3

nums = [1,3,5,6]
target = 5

for index, number in enumerate(nums):
    if number < target:
        continue
    else:
        print(index)
        break

