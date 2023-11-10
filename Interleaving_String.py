# Title: 97. Interleaving String
# Difficulty: Medium
# Problem: https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # handling corner cases
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return True
        if s3 == s1 + s2 or s3 == s2 + s1:
            return True

        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        # all empty strings gives True
        dp[0][0] = True

        for i in range(len(s2) + 1):
            for j in range(len(s1) + 1):
                if i > 0 and dp[i-1][j] and s3[i+j-1] == s2[i-1]:
                    dp[i][j] = True
                    if i+j == len(s3):
                        return True
                if j > 0 and dp[i][j-1] and s3[i+j-1] == s1[j-1]:
                    dp[i][j] = True
                    if i+j == len(s3):
                        return True

        return False
