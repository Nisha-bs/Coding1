#!/usr/bin/python3
intervals = [[1,3],[5,9]]
newinterval = [2,5]
for index, pnt in enumerate(intervals):
    list1 = []
    if len(intervals) > 1 and newinterval[0] > intervals[index][0] and newinterval[0] < intervals[index][1]:
        print(newinterval[0],intervals[index][1])
        #first = intervals[index][0]
        #second = newinterval[1]
        #list1.append(first)
        #list1.append(second)
        intervals.remove(intervals[index])
        #intervals.insert(index,list1)
        print(intervals)
    elif len(intervals) > 1 and newinterval[1] > intervals[index][0] and newinterval[1] > intervals[index][1]:
        #first = intervals[index][0]
        #second = newinterval[1]
        #list1.append(first)
        #list1.append(second)
        #intervals.insert(index,list1)
        #print(intervals)
        intervals.remove(intervals[index])
    elif len(intervals) > 1 and newinterval[1] >= intervals[index][0] and newinterval[1] <= intervals[index][1]:
        second 
