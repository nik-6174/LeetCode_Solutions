# Title: 2870. Minimum Number of Operations to Make Array Empty
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        for value in c.values():
            if value == 1:
                return -1
        min_ops = 0

        for value in c.values():
            count = value

            if count == 2:
                min_ops +=  1
            elif count % 3 == 0:
                min_ops += count // 3
            else:
                min_ops += count // 3 + 1
        return min_ops
