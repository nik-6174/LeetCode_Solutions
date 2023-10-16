# Title: 452. Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the points
        points = sorted(points, key=lambda x: x[1])

        res = 0

        curr = float('-inf')

        for x, y in points:
            if x > curr: # there is no common interval
                res += 1
                curr = y

        return res
