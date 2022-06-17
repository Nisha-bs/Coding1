#!/usr/bin/python3
import re
string = "hello \"how are you?\" friends"
match = re.findall('"(.*?)"',string)
print(match)
