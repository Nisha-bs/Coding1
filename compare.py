#!/usr/bin/python3

list1=["a","ab","abc"]
list2=["bcd","cd","d"]
count = 0
for let in range(len(list1)):
    res = list1[let]
    print(res)
    count = 0
    for character in res:
        print(character)
        if character not in res:
            
            count += 1
        print(count)
        
