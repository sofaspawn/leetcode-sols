#! /usr/bin/env ipython3

class Solution:
    def maxMatrixSum(self, matrix):
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                for dir in dirs:
                    j, i = dir
                    if y+j>=len(matrix) || y+j<0 || x+i>=len(matrix[y]) || x+i<0:
                        continue

        return matrix

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]

s = Solution()
print(s.rotateTheBox(box))
#print(s.rotbox(box))
