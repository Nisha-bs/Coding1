#!/usr/bin/python3
import re

string = '''11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) '''



#text = re.sub("\&\&","and", re.sub("\|\|","or",string))
#print(text)


#string = "hello && hii ||"
string_list = string.split()
#print(string_list)
for word in string_list:
    if word == "&&":
        string = string.replace("&&","and")
#        print(string)
    elif word == "||":
        string = string.replace("||","or")
    else:
        continue
print(string)

