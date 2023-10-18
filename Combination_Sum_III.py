# Title: 216. Combination Sum III
# Difficulty: Medium
# Problem: https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remaining, k, start, current_combination):
            if remaining == 0 and k == 0:
                result.append(current_combination[:])
                return
            if remaining < 0 or k <= 0:
                return
            for i in range(start, 10):
                current_combination.append(i)
                backtrack(remaining - i, k - 1, i + 1, current_combination)
                current_combination.pop()
        
        result = []
        backtrack(n, k, 1, [])
        return result
