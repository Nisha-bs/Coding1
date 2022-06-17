#!/usr/bin/python3
import re
txt = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready."
pattern = re.search("\d+\s\d+",txt)
new_txt = re.sub(r"(?<=\d)\s(?=\d)", '', txt)
#nxt_text = re.sub("(\d+)\s(\d+)","",txt)
print(new_txt)
#print(pattern.string)
