#!/usr/bin/python3
markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist = list(markdict.items())
l=len(marklist)
for i in range(l-1):
    for j in range(i+1,l):
        if marklist[i][1]>marklist[j][1]:
            t=marklist[i]
            marklist[i]=marklist[j]
            marklist[j]=t
    sortdict=dict(marklist)
    print(sortdict)
