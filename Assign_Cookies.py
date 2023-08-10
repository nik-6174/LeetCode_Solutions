# Title: 455. Assign Cookies
# Difficulty: Easy
# Problem: https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort the two arrays
        g.sort()
        s.sort()

        j = 0
        for i in range(len(s)):
            if j < len(g) and g[j] <= s[i]:
                j += 1
        
        return j
