"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for x in range(1, len(nums)):
            nums[x] += nums[x-1] if nums[x-1] > 0 else 0
        return max(nums)


"""
    Best: 

    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            current_subarray = max_subarray = nums[0]
            
            for num in nums[1:]:
                current_subarray = max(num, current_subarray + num)
                max_subarray = max(max_subarray, current_subarray)
                
            return max_subarray
"""