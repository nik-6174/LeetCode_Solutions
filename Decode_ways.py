# Title: 91. Decode Ways
# Difficulty: Medium
# Problem: https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        # no output for cases that start with 0
        if s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)

        # start with 2 ones
        dp[1], dp[0] = 1, 1

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26 and dp[i-2]:
                dp[i] += dp[i-2]

        return dp[-1]
