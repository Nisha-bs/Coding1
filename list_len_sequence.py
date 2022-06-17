#!/usr/bin/python3

list1 = [2,2,10]
list1_length = len(list1)
count = 0

while True:
    for number in range(list1_length):
        for numbers in range(list1_length):
            if numbers+1 != list1[numbers]:
                count += 1
                if list1[numbers] >= numbers + 1:
                    list1[numbers] -= 1
                elif list1[numbers] <= numbers + 1:
                    list1[numbers] += 1
            elif numbers == list1[numbers]:
                break
print(list1)
print(count)
