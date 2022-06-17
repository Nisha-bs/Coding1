#!/usr/bin/python3
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newinterval = [2,5]
res = []

for i in range(len(intervals)):
    if newinterval[0] < intervals[i][0] and newinterval[1] < intervals[i][0]:
        res.append(newinterval)
        res.extend(intervals[i:])
        print(res)
    elif newinterval[0] <= intervals[i][0] or newinterval[0] <= intervals[i][1]:
        newinterval[0] = min(newinterval[0], intervals[i][0])
        newinterval[1] = max(newinterval[1], intervals[i][1])
    else:
        res.append(intervals[i])

#res.append(newinterval)
print(res)
