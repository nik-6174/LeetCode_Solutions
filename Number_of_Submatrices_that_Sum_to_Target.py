# TItle: 1074. Number of Submatrices That Sum to Target
# Difficulty: Hard
# Problem: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        self.target = target
        n, m, res = len(matrix), len(matrix[0])+1, 0

        for i in range(n):
            matrix[i].insert(0, 0)
            for j in range(1, m):
                matrix[i][j] += matrix[i][j-1]

        for i in range(1, m):
            for j in range(i):
                res += self.subarraySum([matrix[idx][i] - matrix[idx][j] for idx in range(n)])
        return res

    def subarraySum(self, nums: List[int]) -> int:
        seen, count, curr = {0: 1}, 0, 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr - self.target in seen:
                count += seen[curr - self.target]
            if curr in seen:
                seen[curr] += 1
            else:
                seen[curr] = 1
        return count
