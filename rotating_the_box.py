#! /usr/bin/env ipython3

class Solution:
    def rotateTheBox(self, box):
        nbox = [row[:] for row in box]
        for y in range(len(nbox)):
            empty = len(nbox[y])-1
            for x in range(len(nbox[y])-1, -1, -1):
                if nbox[y][x]=="#":
                    nbox[y][x], nbox[y][empty] = ".", "#"
                    empty-=1
                elif nbox[y][x]=="*":
                    empty=x-1
        return self.rotbox(nbox)
    def rotbox(self, box):
        nbox = []
        x = 0
        while x<len(box[0]):
            y = len(box)-1
            row = []
            while y>=0:
                row.append(box[y][x])
                y-=1
            nbox.append(row)
            x+=1
        return nbox

box = [["#","#","*",".","*","."],
       ["#","#","#","*",".","."],
       ["#","#","#",".","#","."]]

s = Solution()
print(s.rotateTheBox(box))
#print(s.rotbox(box))
