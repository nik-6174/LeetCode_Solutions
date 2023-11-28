# Title: 516. Longest Palindromic Subsequence
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def lps(i, j):
            if i == j:
                return 1
            elif i + 1 == j and s[i] == s[j]:
                return 2
            elif s[i] == s[j]:
                return lps(i+1, j-1) + 2
            
            return max(lps(i+1, j), lps(i, j-1))
        
        return lps(0, len(s)-1)
