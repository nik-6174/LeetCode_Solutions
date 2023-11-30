# Title: 828. Count Unique Characters of All Substrings of a Given String
# Difficulty: Hard
# Problem: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # create a dict of indices for each character
        graph = defaultdict(list)
        for idx, char in enumerate(s):
            graph[char].append(idx)
        
        count = 0
        for indices in graph.values():
            # we add -1 and len(s) to take care of the corner cases
            indices = [-1] + indices + [len(s)]
            for i in range(1,len(indices)-1):
                # all unique orrcurances is the product of difference of last and present occurance
                # and difference of next and previous occurances
                count += (indices[i] - indices[i-1]) * (indices[i+1] - indices[i])
        return count
