# Title: 692. Top K Frequent Words (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Sort the Counter items based on frequency and lexicographically
        sorted_items = sorted(Counter(words).items(), key=lambda item: (-item[1], item[0]))

        # Extract the keys from the sorted items to get the top k frequent words
        res = [item[0] for item in sorted_items[:k]]

        return res
