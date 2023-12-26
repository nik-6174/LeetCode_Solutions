# Title: 1155. Number of Dice Rolls With Target Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # use moization using cache function
        @cache
        def find(n: int, target: int) -> int:
            if n < 0 or target < 0: return 0 # zeros ways
            if target == 0 and n == 0:
                return 1 # one way
            total = 0
            for i in range(1, k+1):
                total += find(n-1, target-i) # add all the number ways
            return total % (10 ** 9 + 7)
        return find(n, target)
