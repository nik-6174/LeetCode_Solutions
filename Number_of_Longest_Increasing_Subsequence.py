# Title: 673. Number of Longest Increasing Subsequence
# Difficulty: Medium
# Problem: https://leetcode.com/problems/number-of-longest-increasing-subsequence/description

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        max_length = 1 # keep track of the longest subsequence length

        # find the max subsequence length and the count for the given length
        for i in range(len(nums)-2, -1, -1):
            countMax = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[i] < 1 + dp[j]: # new maximum
                        dp[i] = 1 + dp[j]
                        countMax = count[j] # count for j is also count for i
                    elif dp[i] == 1 + dp[j]:
                        countMax += count[j] # add the count for j to count for i
            count[i] = countMax
            max_length = max(max_length, dp[i])

        # return the sum of the counts that has the max_length of subsequence
        return sum([count[i] for i in range(len(nums)) if dp[i] == max_length])
