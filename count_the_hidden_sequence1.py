#!/usr/bin/python3

differences = [1, -3, 4]
lower = 1
upper = 6
range_list = []

#differences = [1, -3, 4]
print(differences)
for digit in range(1,upper+1):
    range_list.append(digit)
print(range_list)

list1 = []
x = 0
for i in range(len(range_list)+1 - 1):
    for j in range(len(range_list)+1 - 1):
        print(range_list[i], range_list[j])
        sub = range_list[i] - range_list[j]
        if differences[x] == sub:
            print("diff, sub" ,differences[x], sub)
            if len(list1) == 0:
                list1.append(range_list[j])
                insert2 = range_list[i]
                list1.append(insert2)
                x += 1
                print(list1)
            else:
                list1.append(range_list[j])
                print(list1)
        else:
            continue

        value = list1[len(list1)-1]
        print("value", value)
        for k in range(len(range_list) - 1):
            sub1 = range_list[k] - value
            #print("diff, sub1", differences[x], sub1)
            if differences[x] == sub1:
                list1.append(range_list[k])
            else:
                continue

print(list1,value)

