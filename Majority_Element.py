#!/usr/bin/python3

nums = [3,2,3]
value_count_list = []
for value in nums:
    value_count = nums.count(value)
    value_count_list.append(value_count)
    max_value = max(value_count_list)
    index_value = value_count_list.index(max_value)
print(nums[index_value])
print("index_value", index_value,max_value,"max_value")
if nums[index_value] > len(nums)/2:
    print(nums[index_value])
else:
    print("0")

