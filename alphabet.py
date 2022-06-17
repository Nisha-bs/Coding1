#!/usr/bin/python3

alp = ["d","b","a","a","b","c","c","a","c","d","c","b","d","d","a"]
alp_dict = {}
'''for index in range(len(alp)):
    count = 0
    if alp[index] not in alp_dict:
        alp_dict[alp[index]]=0
    alp_dict[alp[index]]+= 1
print("alp_dict",alp_dict)
'''
for itm in alp:
    if itm in alp_dict.keys():
        alp_dict[itm] = alp_dict[itm] + 1
    else:
        alp_dict[itm] = 1

print(alp_dict)
alp_list = list(alp_dict.items())
l=len(alp_list)
for ind in range(l-1):
    for pos in range(ind+1,l):
        if alp_list[ind][1] < alp_list[pos][1]:
            t=alp_list[ind]
            alp_list[ind]=alp_list[pos]
            alp_list[pos]=t
        elif alp_list[ind][1] == alp_list[pos][1]:
            if ord(alp_list[ind][0]) > ord(alp_list[pos][0]):
                t=alp_list[ind]
                alp_list[ind]=alp_list[pos]
                alp_list[pos]=t
sort_dict=dict(alp_list)
print(sort_dict)
