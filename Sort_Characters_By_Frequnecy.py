# Title: 451. Sort Characters By Frequency (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        # find the characters and their frequency
        counter = Counter(s)
        # sort the character based on their frequency
        sorted_dict = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

        res = ''
        # create a string adding the characters with frequency in decreasing order
        for elem in sorted_dict:
            res += elem*sorted_dict[elem]
        
        return res
