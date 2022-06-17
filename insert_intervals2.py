#!/usr/bin/python3
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [2,5]
res = [newInterval]
for interval in intervals:
    if interval[1] < res[-1][0]:
        res.insert(-1, interval)
    elif interval[0] > res[-1][1]:  # res[-1][0] <= interval[1]
        res.append(interval)
    elif interval[0] < newInterval[0]  and interval[1] < newInterval[1]:
        res.pop(interval)
    else:
        res[-1][0] = min(interval[0], res[-1][0])
        res[-1][1] = max(interval[1], res[-1][1])

print(res)
