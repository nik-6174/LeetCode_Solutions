# Title: 462. Minimum Moves to Equal Array Elements II (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()

        # let's find the median for minumum moves
        median = 0
        if len(nums) % 2 == 1:
            median = nums[(len(nums) - 1)//2]
        else:
            median = (nums[len(nums)//2] + nums[len(nums)//2-1])//2
        
        # return the difference of nums from median
        return sum([abs(num - median) for num in nums])
        

