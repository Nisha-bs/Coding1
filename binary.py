#!/usr/bin/python3
'''
n = 2
range_value = ((2)**n) - 1 
print(range_value)
bin_value = bin(range_value)[2:]
length = len(bin_value)
print("length, bin_value", length,bin_value)
binary_list = []


for number in range(range_value + 1):
    binary_number = bin(number)[2:]
    #print(bin(number))
    binary_number_length = len(binary_number)
    #print("binary_number_length", binary_number_length)
    if binary_number_length < length:
        for append_value in range(length - binary_number_length):
            binary_number = "0" + binary_number 
        binary_list.append(binary_number)
    else:
        binary_list.append(binary_number)
print(binary_list)

i = 1
for index, bin_val in enumerate(binary_list):
    #print(binary_list[bin_val])
    count = 0
    for bit_index, bit in enumerate(bin_val):
        #print(binary_list[bin_val][bit])
        if bin_val[bit_index] != bin_val[bit_index]:
            count += 1
            if count >= 2:
                i += 1
                bin_val -= 1
                break
            else:
                continue
        else:
            continue
    if count == 1:
        pass
    else:
        temp = binary_list[index] 
        binary_list[index ] = binary_list[index]
        binary_list[index ] = binary_list[index]
print(binary_list)
'''
'''
n = 2
ans = []
for i in range(0, 2 ** n):
    b = bin(i)[2:]
    temp = b[0]
    for j in range(1, len(b)):
        temp += str(int(b[j - 1]) ^ int(b[j]))
    ans.append(temp)

print(list(map(lambda x: int(x, 2), ans)))
'''

new_list = []
new_list.append(binary_list(0))
for index, bin_val in enumerate(binary_list):
    for bit_index in enumerate(bin_val):



