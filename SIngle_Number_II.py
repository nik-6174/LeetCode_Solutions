# Title: 137. Single Number II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/single-number-ii/description

# Using bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ones, twos = 0, 0

        for num in nums:
            # Update 'ones' to keep the bits that appear once
            ones = (ones ^ num) & ~twos

            # Update 'twos' to keep the bits that appear twice
            twos = (twos ^ num) & ~ones

        return ones

# Using list
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        # sort the array
        nums.sort()
        # handles cases where the number is the smallest or the largest
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        
        for i in range(1,len(nums)-1):
            # check when the neighbours are not equal to an element
            if nums[i-1] != nums[i] and nums[i+1] != nums[i]:
                return nums[i]
        return
        
            


        
