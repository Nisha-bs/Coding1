#!/usr/bin/python3
import re
string = '<p>Contents :</p><a href="https://www.w3resource.com">Python Examples</a><a href="http://www.github.com">Even More Examples</a>'

check = re.findall(r'((https|http)(:\/\/www\..{2,256}?)(\.com|\.org|\.dev))',string)

print(check.groups(1))
