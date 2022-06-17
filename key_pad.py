#!/usr/bin/python3
digits = "23"
dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
ans = []
if not digits:
    print([])
for i in range(len(digits)):
    if ans == []:
        ans += dic[digits[i]]
    else:
        temp = []
        for j in range(len(ans)):
            for k in range(len(dic[digits[i]])):
                temp.append(ans[j] + dic[digits[i]][k])
            ans = temp
print(ans)
