# Title: 1456. Maximum Number of Vowels in a Substring of Given Length (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # creat a set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # map the vowels in the string to 1 else zeroes
        mapped = [1 if i in vowels else 0 for i in s]
        # calculate the number of vowels in the first k places in the string; also initialize it as the maximum number of vowels
        max_vowels = no_of_vowels = sum(mapped[:k])
        
        for i in range(len(s)-k):
            # calculate the number of vowels in the next iteration
            no_of_vowels += mapped[i+k] - mapped[i]
            if no_of_vowels > max_vowels: # if number of vowels in the next iteration is greater then the max number seen so far, the update the max number
                max_vowels = no_of_vowels
        return max_vowels
