#! /usr/bin/env python3
def soln(height):
    '''
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Z = x * y

    maximize Z

    '''
    # O(n^2)
    '''
    urr = 0
    for i in range(len(height)):
        for j in range(i,len(height)):
            area = (j-i) * min(height[i], height[j])
            if area>urr:
                urr = area
    return urr
    '''





#print(soln([1,8,6,2,5,4,8,3,7]))
print(soln([1,1]))
