'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
배열안에 두개의 값을 더해서 target이 되게 만들어라
'''

'''
from typing import List
class Solution:
    nums    = [2,7,11,15]
    target  = 9
    print(nums)
    # Why does the "self" element exist?
    def twoSum(self, nums : List[int], target : int): 
        lnums = len(nums)
        for i in range(lnums):
            for j in range(i+1, lnums):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return []
    
    aResult = twoSum(1,[2,7,11,15], 9)
    print(aResult)
'''
from typing import List
class Solution:
    # nums = [2,7,11,15]
    # target = 9
    def twoSum(self, nums : List[int], target : int):
        print('test')
        hNums = {}
        for i in range(len(nums)):
            if target - nums[i] not in hNums:
                hNums[nums[i]] = i 
            else:
                return [hNums[target - nums[i]], i]
        return []
    
    result = twoSum(1, [2,7,11,15], 9)
    print(result)
    