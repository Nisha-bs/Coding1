#!/usr/bin/python3

numerator = 1
denominator = 2

div = numerator/denominator
#print(div)

split_value = str(div).split(".")
print(split_value[1])
if len(split_value[1]) > 1:
    print(split_value[0] + "." +  "(" + split_value[1] + ")")
else:
    print(div)
