#!/usr/bin/python3

lower = 1
upper = 6
range_list = []
final_list = []


differences = [1, -3, 4]
print(differences)
for i in range(1,upper+1):
    range_list.append(i)
print(range_list)

i = 0
for jump in range(len(range_list)):
    list1 = []
    for val in range(len(range_list) - 1):
        sub = range_list[val] - range_list[jump]
        for index, values1 in enumerate(differences):
            if sub == differences[i]:
                insert1 = range_list[jump]
                list1.insert(index, insert1)
                insert2 = range_list[val]
                list1.insert(index + 1, insert2)
                final_list.append(list1)
                val = range_list[val]
                for values in range(len(range_list)):
                    sub1 = range_list[ values ] - val
                    if sub1 == range_list[jump]:
                        list1.insert(len(list1), range_list[values])
                    else:
                        continue
            else:
                continue
print(final_list)
