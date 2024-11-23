#! /usr/bin/env python3

class Solution:
    def soln(self,s):
        freq = {}
        i = 0
        j = 0
        lens = []
        while j<len(s):
            while i<len(s):
                if s[i] in freq:
                    lens.append(len(list(freq.keys())))
                    freq = {}
                freq[s[i]]=1
                i+=1
            j+=1
            i=j
        lens.append(len(list(freq.keys())))
        if lens:
            return max(lens)
        else:
            return len(s)

#s = "dvdf"
s = "asjrgapa"
sol = Solution()
print(sol.soln(s))
