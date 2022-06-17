#!/usr/bin/python3
test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]} 
dict_values = test_dict.values()
print(dict_values)
number_list = list(set([char for sub_list in dict_values for char in sub_list]))
print(number_list)
output_dict = {}
for number in number_list:
    temp_list = []
    for key, value in test_dict.items():
        if number in value:
            temp_list.append(key)
    output_dict[number] = temp_list
print(output_dict)
