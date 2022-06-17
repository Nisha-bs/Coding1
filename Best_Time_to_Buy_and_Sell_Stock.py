#!/usr/bin/python3

k = 4
prices = [3,2,6,8,0]
count = 0
profit_list = []
profit = 0

'''
for money in range(len(prices)-1):
    if prices[money] < prices[money+1]:
        sub = prices[money + 1] - prices[money]
        #profit_list.append(profit)
        #count += 1
        profit += sub
    else:
        continue
print(profit)
'''

for money in range(len(prices)):
        count = 0
        for start in range(money, len(prices)-1):
            #if prices[start] < prices[start+1]:
                sub = prices[start + 1] - prices[start]
                count += 1
                profit += sub
                #profit_list.append(profit)
                #print(count)
                if count == k//2:
                    break
                else:
                    continue
            #else:
             #   continue
print(profit)

