#!/usr/bin/python3
import re
string = "hello hii nisha 11223, how are u nisha"

output = re.search(r"\d+",string)
print(output.start())

print(output.end())

print(output.span())

