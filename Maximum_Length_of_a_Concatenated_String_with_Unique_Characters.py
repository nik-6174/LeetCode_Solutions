# Title: 1239. Maximum Length of a Concatenated String with Unique Characters
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = [set([char for char in arr[i]]) for i in range(len(arr))]
        not_unique = set([i for i in range(len(arr)) if len(arr[i]) != len(sets[i])])
        seen = set()

        def dfs(start):
            if start == len(arr):
                return 0
            res = dfs(start+1)
            if start in not_unique or sets[start] & seen:
                return res
            seen.update(sets[start])
            res = max(res, len(arr[start]) + dfs(start+1))
            seen.difference_update(sets[start])
            return res
            
        return dfs(0)
