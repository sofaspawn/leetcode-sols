#! /usr/bin/env python3

def soln(s):
    freq = {}
    i = 0
    lens = []
    if len(s)==1:
        return 1
    while i<len(s):
        if s[i] in freq:
            lens.append(len(list(freq.keys())))
            freq = {}
        freq[s[i]]=1
        i+=1
    return max(lens)

s = "pwwkew"
print(soln(s))
