#!/usr/bin/python3
s = "aaaabbbbcccc"
substring = ''
dict_s = {}
list_s = []
#while len(s) > 0:
for index, letter in enumerate(s):
    dict_s[letter] = ord(s[index])
    list_s.append(letter)
    #print(dict_s,list_s)
smallest = min(dict_s.keys())
largest = max(dict_s.keys())
#print(largest,smallest)
while len(list_s) <= len(s):
    for value, charac in enumerate(list_s):
        if charac == smallest:
            substring += charac
            list_s.remove(charac)
            #print('first',list_s,substring)
            break
        else:
            continue
    for value1, charac1 in enumerate(list_s):
        if charac1 != smallest and charac1 > smallest and charac1 < largest:
            substring += charac1
            list_s.remove(charac1)
            #print('second',list_s,substring)
            break
        else:
            continue
    for value2, charac2 in enumerate(list_s):
        if charac2 > smallest and charac2 == largest:
            substring += charac2
            list_s.remove(charac2)
            #print('third',list_s, substring)
            break
        else:
            continue
    for value3, charac3 in enumerate(list_s):
        if charac3 > smallest and charac3 == largest:
            substring += charac3
            list_s.remove(charac3)
            #print('third',list_s, substring)
            break
        else:
            continue
    for value4, charac4 in enumerate(list_s):
        if charac4 > smallest and charac4 < largest:
            substring += charac4
            list_s.remove(charac4)
            #print('second',list_s,substring)
            break
        else:
            continue
    for value5, charac5 in enumerate(list_s):
        if charac5 == smallest:
            substring += charac5
            list_s.remove(charac5)
            #print('first',list_s,substring)
            break
        else:
            continue
    else:
        break
print(substring)
