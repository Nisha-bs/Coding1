#!/usr/bin/python3

a = 1
b = 2
n = 10
print(a,b, end = " " )

while n - 2:
    c = a + b
    a = b
    b = c
    print(c, end = " ")
    n = n - 1
