#!/usr/bin/python3

number = 1

power = len(str(number))
sums = 0
temp = number
while temp > 0:
    digit = temp % 10
    sums = sums + digit ** power
    temp//=10

if sums == number:
    print("Amstrong number")
else:
    print("Not an amstrong number")
