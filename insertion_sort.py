#!/usr/bin/python3

head = [3,8,6,7,4,2,1]
'''for ind in range(1,len(head)):
    store = head[ind]
    create_list = head[:ind]
    #print(create_list)
    for ele in create_list:
        mini = max(create_list)
        mini_index = head.index(mini)
        print(mini, mini_index)

        if store < mini:
            head[ind] = head[ind-1]
            ind = ind -1
        head[ind] = store
    else:
        continue
print(head)
'''
for index in range(1,len(head)):

    currentvalue = head[index]
    position = index

    while position > 0 and head[position-1] > currentvalue:
        head[position] = head[position-1]
        position = position-1

    head[position]=currentvalue


print(head)

