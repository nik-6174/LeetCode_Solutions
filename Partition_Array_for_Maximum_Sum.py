# Title: 1043. Partition Array for Maximum Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/partition-array-for-maximum-sum/description

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1,n+1):
            j = i-1
            max_val = arr[i-1]
            while j > i-k-1 and j >= 0:
                max_val = max(max_val, arr[j])
                dp[i] = max(dp[i], max_val * (i - j) + dp[j])
                j -= 1
        
        return dp[-1]
