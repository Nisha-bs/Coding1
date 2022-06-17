#!/usr/bin/python3
import re
string = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
#consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
consonants = "QWRTYPSDFGHJKLZXCVBNM"
#vowels = "AEIOUaeiou"
vowels = "aeiou"

#output = re.findall(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]",string)
#output = re.findall(r'([%s])([%s]{2,})([%s])'%(consonants,vowels,consonants),string)
#output = re.findall(r'(?<=[consonants])([vowels]{2,})(?=[consonants])',string)
output = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',string,flags = re.I)
print(output)
