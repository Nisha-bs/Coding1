#!/usr/bin/python3

from itertools import permutations
x = 'god'
perms = []
list1=[]
for i in range(1, len(x)+1):
    print(i)
    for c in permutations(x, i):
        print(c)
        perms.append("".join(c))
        print(perms)

        for word in perms:
            if len(word) == len(x):
                if word not in list1:
                    list1.append(word)

print(list1)
