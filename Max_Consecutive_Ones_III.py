# Title: Max Consecutive Ones III (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # initialize the variables to check and save the max count
        max_count = 0
        start = 0
        # use a sliding window to increase in length at each index where it has consecutive 1s or till it has exhausted k 0s
        for idx, num in enumerate(nums):
            if not num:
                if k:
                    k -= 1
                else:
                    while nums[start]:
                        start += 1
                    start += 1
            max_count = max(idx+1 - start, max_count) # update the max count
        return max_count
