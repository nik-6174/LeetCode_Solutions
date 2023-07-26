# Title: 720. Longest Word in Dictionary (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-word-in-dictionary/description/

# using heapq library, and min heap data structure
import heapq

class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = []
        s = set(words)
        max_len = 0
        
        # Step 1: Finding all valid words and the maximum length among them
        for word in s:
            flag = True
            for i in range(len(word)-1, 0, -1):
                # Check if the prefix of the word (excluding last character) is not in the set
                if word[:i] not in s:
                    flag = False
                    break
            if flag:
                max_len = max(max_len, len(word))
                res.append(word)

        # If there is no answer (no valid words found)
        if not res:
            return ''

        # Step 2: Create a min-heap to store the lexicographically smallest words
        smallest_heap = []

        # Step 3: Iterate through the valid words and add words with the highest length to the heap
        for word in res:
            if len(word) == max_len:
                heapq.heappush(smallest_heap, word)

        # Step 4: The smallest lexicographically word is the root of the heap
        return smallest_heap[0]


# using just set
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = []
        s = set(words)
        for word in s:
            flag = True
            for i in range(len(word)-1, 0, -1):
                if word[:i] not in s:
                    flag = False
                    break
            if flag:
                res.append(word)

        # if there is no answer
        if not res:
            return ''

        return sorted(res, key=lambda item: (-len(item), item))[0]
