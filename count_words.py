#!/usr/bin/python3

startwords = ["ant","act","tack"]
targetwords = ["tack","act","acti"]

for t_word in targetwords:
    for s_word in startwords:
        if s_word in t_word:
            if len(s_word) != len(t_word):
                print(s_word)
                print(t_word)
                for t_let in t_word:
                    if t_let not in s_word:
                        print(t_let)
              
