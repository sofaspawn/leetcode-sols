#! /usr/bin/env python3

def soln(nums, k):
	i = 0
	j = i+k
	arr = []
	count = 0
	while i<len(nums)-k+1:
		arr = nums[i:j]
		if len(set(arr))==len(arr):
			print(arr)
			print(sum(arr))
			count = max(count, sum(arr))
		i+=1
		j+=1
	return count

'''
nums = [1,5,4,2,9,9,9]
k = 3
'''

nums = [1,1,1,7,8,9]
k = 3

print(soln(nums,k))

