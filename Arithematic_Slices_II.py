# Title: 446. Arithmetic Slices II - Subsequence
# Difficulty: Hard
# Problem: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        dp = [defaultdict(int) for _ in nums]

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  # Initialize with 1 for every valid diff
                if diff in dp[j]:  # Continue building on previous subsequences
                    dp[i][diff] += dp[j][diff]
                    count += dp[j][diff]  # Accumulate the count

        return count
