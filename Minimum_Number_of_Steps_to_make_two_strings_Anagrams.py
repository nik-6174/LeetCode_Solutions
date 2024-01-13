# Title: 1347. Minimum Number of Steps to Make Two Strings Anagram
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i])-ord('a')] += 1
            counter[ord(t[i])-ord('a')] -= 1
        
        # find the difference in the count of each character, and then divide it by 2
        abs_sum = 0
        for i in range(26):
            abs_sum += abs(counter[i])
        
        return abs_sum // 2
