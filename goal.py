#!/usr/bin/python3
nums = [1,-10,9,1]
limit = 100
goal = 0


#req = goal - sum(nums)
res = 0
for numbers in nums:
    res += numbers
#print(res)
req = goal - res


if req==0:
	print("0")

count=0
while req!=0:
    new = (abs(req)//limit)
    count+=new
    new = new*limit
    if req<0:
        req = req+new
    else:
        req = req-new
    if abs(req)<=limit and req!=0:
        print(count+1)
    break
