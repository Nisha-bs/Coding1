#!/usr/bin/python3

#num = 4
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)
print(fact(6))
