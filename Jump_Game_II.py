# TItle: 45. Jump Game II (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))

        # find the minimum number of steps starting from the last index
        for i in range(len(nums)-2, -1, -1):
            if nums[i]: # when nums[i] is not 0
                dp[i] = 1 + min(dp[i+1: min(i+1+nums[i], len(nums))])
            else: # when nums[i] is 0
                dp[i] = 100000
        # return minimum steps from the start index
        return dp[0]
