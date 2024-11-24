#! /usr/bin/env python3

class Solution:
    def findTheDifference(self, s, t):
        s = "".join(sorted(list(s)))
        t = "".join(sorted(list(t)))
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i] 
        return t[-1]

s = "a"
t = "aa"

sol = Solution()
print(sol.findTheDifference(s,t))
#print(s.rotbox(box))
