#!/usr/bin/python3
import re
string = "Python_ExerciseProblem"
match1 = re.findall(r'[A-Z][a-z]+',string)
print(match1)
