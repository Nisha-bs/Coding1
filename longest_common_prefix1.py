#!/usr/bin/python3
strs = ["flower","flow","floght","flot"]
min_length = 200
for word in strs:
    min_length = min(min_length, len(word))
    print(min_length)
strs.sort()
print(strs)
common_prefix, i = "", 0
first, last = strs[0], strs[-1]
print(first, last)
while i < min_length and first[i] == last[i]:
    common_prefix += strs[0][i]
    print(common_prefix)
    i += 1
print(common_prefix)
