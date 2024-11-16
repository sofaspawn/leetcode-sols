#! /usr/bin/env python3
def soln(nums, target):
    '''
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    Input: nums = [1,3,5,6], target = 2
    Output: 1
    '''
    if target<=nums[0]:
        return 0
    for i in range(len(nums)-1):
        if nums[i]==target:
            return i
        if nums[i+1]>target and nums[i]<=target:
            return i+1
    if target==nums[-1]: return len(nums)-1
    return len(nums)


print(soln([1,3,5,6], 7))
