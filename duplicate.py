#!/usr/bin/python3

nums = [1,2,3,4,2,3]

for ele in range(len(nums)):
    for elemnt in range(ele+1,len(nums)):
        if nums[elemnt] == nums[ele]:
            print(nums[ele])

