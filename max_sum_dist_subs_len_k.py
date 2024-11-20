#! /usr/bin/env python3

def soln(nums, k):
    i = 0
    j = i+k
    arr = []
    count = 0
    prev = sum(nums[i:j])
    i+=1
    j+=1
    while i<len(nums)-k+1:
        arr = nums[i:j]
        if len(set(arr))==len(arr):
            n = prev - nums[i-1] + arr[-1]
            count = max(count, n)
        i+=1
        j+=1
    return count

'''
nums = [1,5,4,2,9,9,9]
k = 3
'''
nums = [4,4,4]
k = 3
'''
nums = [1,1,1,7,8,9]
k = 3
'''

print(soln(nums,k))

