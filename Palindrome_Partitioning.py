# Title: 131. Palindrome Partitioning
# Difficulty: Medium
# Problem: https://leetcode.com/problems/palindrome-partitioning/description

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def findPlaindromicSubstring(start):
            if start == len(s): return [[]]
            if start == len(s) - 1: return [[s[-1]]]
            res = []
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    partitions = findPlaindromicSubstring(i+1)
                    if not partitions: continue
                    res += [[s[start:i+1]] + partition for partition in partitions]
            return res
        return findPlaindromicSubstring(0)
