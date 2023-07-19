# Title: 334. Increasing Triplet Subsequence (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if there are less than 3 values, return False
        if len(nums) < 3:
            return False
        
        smallest = float('inf')  # Smallest number found so far
        second_smallest = float('inf')  # Second smallest number found so far
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True  # We found a third number greater than the first two
        
        return False
