#!/usr/bin/python3
import itertools

def key_pad(number):
    keypad = {2 : 'abc',3 :'def' ,4 : 'ghi' ,5 : 'jkl' , 6 : 'mnop' , 7 : 'qrst' , 8 : 'uvw' , 9 : 'xyz'}
    #number = input("enter the number")

    for digit in number:
        print(digit)
        keypad_keys = keypad.keys()
        print(keypad_keys)
        for keys in keypad_keys:
            if digit in keypad_keys:
                print("yes")

key_pad("23")
