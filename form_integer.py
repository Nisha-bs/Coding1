#!/usr/bin/python3

num = [1,2,0,0]
k = 34
integer = ""
for numbers in num:
    conv = str(numbers)
    integer += conv 
output = int(integer) + k
str_output = str(output)
final_list = []
for element in str_output:
    final_list.append(int(element))
print(final_list)
