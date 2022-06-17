#!/usr/bin/env python3

with open("data.txt", "r") as f:
     data = list(map(list,f.read().splitlines()))
     print(data)
result =""

def find_loc (word,data,result):
   for row,sentence in enumerate(data):
       temp_list =[]
       temp="".join(sentence)
       print(temp)
       if word in temp:
           temp_list.append(row)
           temp_list.append(temp.find(word))
           temp_list.append(temp_list[-1]+len(word))
           result.append(temp_list)
 

output_list =[]
find_loc("uA",data,output_list)

def extract(row,data): 
     result = ""
     for col in range(len(data[row])):
        if  col <26:
           result+=data[row][col]
     return result

for i in output_list:

    print(extract(i[0],data))


