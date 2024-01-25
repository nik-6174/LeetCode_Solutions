# Title: 1143. Longest Common Subsequence
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-common-subsequence/description

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a DP table to store the LCS lengths for subproblems
        dp = [[0] * (n + 1) for _ in range(2)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[1][j] = dp[0][j - 1] + 1
                else:
                    dp[1][j] = max(dp[0][j], dp[1][j - 1])
            
            # initialize the next row as zeroes and swap the rows
            for x in range(n + 1):
                dp[0][x], dp[1][x] = dp[1][x], 0

        return dp[0][n]
