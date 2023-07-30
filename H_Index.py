# Title: 274 H-Index
# Difficulty: Medium
# Problem: https://leetcode.com/problems/h-index/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort the citations in descending order
        n = len(citations)
        h_index = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index
