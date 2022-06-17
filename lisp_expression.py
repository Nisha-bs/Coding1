#!/usr/bin/python3

text = "(+5(*342)5)"
txt = []
for ele in text:
    txt.append(ele)
print(txt)

#txt = text.split(" ")
#print(txt)

stack = []

operations = "+-*/"
open_bracket = "{(["
close_bracket = "})]"
result = 0

for index, val in enumerate(txt):
    if val in operations:
        stack.append(val)
    elif val in open_bracket:
        stack.append(val)
    elif val in close_bracket:
        loop = True
        operands = []
        op = ""
        value = 0
        while loop:
            print("stack", stack)
            item = stack.pop(-1)
            print("stack items", item)
            if item in open_bracket:
                loop = False
            elif item in operations:
                op = item
            else:
                operands.append(item)
        operands = [int(d) for d in operands]

        print(operands)
        if op == "+":
            value = sum(operands)
            print(value)
        elif op == "*":
            value = 1
            for d in operands:
                value *= d
        stack.append(str(value))
        result = value
    else:
        stack.append(val)
print(result)

