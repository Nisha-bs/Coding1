#!/usr/bin/python3
import itertools
s = "eleetminicoworoep"
'''vowels = "aeiou"

for i in range(len(s)):
    for j in range(len(s)):
        string = s[i:j+1]
    print(string)
    for k in range(len(s),i):
        string = s[k+1:i]
    print(string)
'''












'''
for letter in s:
    if letter  not in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] += 1
print(letter_count)
'''






'''
for char in range(len(s)):
    letter_count = {}
    string = s[: len(s)-char]
    #print(string)
    for letter in string:
        if letter in vowels:
            if letter  not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
        else:
            continue
    #print(letter_count)
    print(string)
    init = 0
    length = len(letter_count)
    #print("length",length)
    for count_value in letter_count.values():
        #print("count_value",count_value)
        init += 1
        if count_value % 2 == 0 and init == length:
            #print(string)
            init = 0
        elif count_value % 2 == 0 and init != length:
            continue
        else:
            break

'''

#import itertools
#letters = 'god'
combinations = []
for i in range(len(s)):
    combinations.extend([''.join(x) for x in itertools.permutations(s, i + 1)])
print(combinations)
