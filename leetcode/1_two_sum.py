"""
Contains the solution for Leetcode Problem 1. Two Sum, found at: https://leetcode.com/problems/two-sum/

Two attempts were made at solving the problem. Both run in O(n), the second attempt just runs faster 
since it loops through nums only once. 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # First Attempt
        # Convert the nums to a dict, where key = num and value = index
        # nums_dict = {}
        # nums_set = set()
        # for i in range(0, len(nums)):
        #     nums_set.add(nums[i])
        #     nums_dict[nums[i]] = i
        
        # Now iterate through the nums, check if the target - num is in sums_set
        # for i in range(0, len(nums)):
        #     left = target - nums[i]
        #     if left in nums_set and nums_dict[left] != i:
        #         return [i, nums_dict[left]]
            
        # Second Try
        nums_dict = {}
        for i in range(0, len(nums)):
            left = target - nums[i]
            if left in nums_dict.keys():
                return [i, nums_dict[left]]
            else:
                nums_dict[nums[i]] = i
