#!/usr/bin/python3

people = [1,1,1,1,1,1,1]
limit = 3

for index1 in range(len(people)):
    for index2 in range(index1+1,len(people)):
        if people[index1] > people[index2]:
            temp = people[index1]
            people[index1] = people[index2]
            people[index2] = temp
print(people)

boat=0

right=len(people)-1
left=0

while right>=left:
    if people[right]+people[left]>limit:
        boat+=1
        right-=1

    elif people[right]+people[left]<limit:
        count_people = people[right]+people[left]
        right -= 1
        count_people = count_people + people[right]
        if count_people > limit:
            boat += 1
            right -= 1
        else:
            boat += 1
            right -= 1
            left += 1
    else:
        boat+=1
        right-=1
        left+=1
print(boat)


