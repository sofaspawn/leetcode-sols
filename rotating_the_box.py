#! /usr/bin/env ipython3

class Solution:
    def rotateTheBox(self, box):
        nbox = self.rotbox(box)
        y = len(nbox)-1
        while y>=0:
            x = 0
            while x<len(nbox[y]):
                if y+1>=len(nbox):
                    x+=1
                    continue
                else:
                    if nbox[y+1][x]=="." and nbox[y][x]=="#":
                        nbox[y+1][x] = nbox[y][x]
                        nbox[y][x] = "."
                    x+=1
            y+=1
        return nbox
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
