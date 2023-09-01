# Title: 747. Largest Number At Least Twice of Others
# Difficulty: Easy
# Problem: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_largest = [-1, 0]
        second_largest = [-1, 0]


        for i in range(len(nums)):
            if nums[i] > second_largest[1]:
                second_largest = [i, nums[i]]
                if second_largest[1] > first_largest[1]:
                    first_largest, second_largest = second_largest, first_largest
        
        if first_largest[1] >= 2*second_largest[1]:
            return first_largest[0]
        else:
            return -1
