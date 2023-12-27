# Title: 1578. Minimum Time to Make Rope Colorful
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_color, max_time, res = colors[0], neededTime[0], sum(neededTime)

        # so that the end is considered in the loop with the color change
        colors += "X"
        neededTime.append(0)

        for i in range(len(colors)):
            if colors[i] == prev_color: # when there are consecutive color balloons
                max_time = max(max_time, neededTime[i])
            else: # when a new color balloon is encountered
                res -= max_time
                max_time = neededTime[i]
                prev_color = colors[i]

        return res
