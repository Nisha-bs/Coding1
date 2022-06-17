#!/usr/bin/env python3

user_input = [2,2,2,2,2]
result_list = [ i+1 for i in range(len(user_input))]
print(result_list)
count=0

while user_input != result_list:  
      for index in range(len(user_input)):
          if user_input[index] == result_list[index]:
              continue
          elif user_input[index] > result_list[index]:
               user_input[index]-=1
          elif user_input[index] < result_list[index]:
               user_input[index]+=1 
      count+=1
print(count)
