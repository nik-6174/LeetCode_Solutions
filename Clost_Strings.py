# 1657. Determine if Two Strings Are Close (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)
        # check if the letters are same, and if the number of occuranced of letters is same
        if sorted(d1.values()) != sorted(d2.values()) or d1.keys() != d2.keys():
            return False
        # if the letters are same, and if the sorted number of occurances of each letter is same, then return True
        # since we can always swap the elements and permute them after that to get the other word by swapping the position of elements
        return True
