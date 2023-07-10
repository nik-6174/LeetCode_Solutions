# Title: 2390. Removing Stars From a String (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        # create a stack
        res = []
        for char in s:
            # is the character is * then  we pop the stack
            if char == '*':
                res.pop()
            else:
            # we append non-start characters
                res.append(char)
        return ''.join(res) # we return the string after joining all characters into a list
