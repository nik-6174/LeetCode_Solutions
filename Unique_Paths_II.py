# Title: Unique Paths II (LeetCode)
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        # create a grid with padding of 1 unit with all 0s
        dp = [[0]*(len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        # number of ways to read the starting place is trivial
        dp[1][1] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
              # skip the starting point
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0: # when the value if 0, i.e., free space, fill the value with the sum of the ways it's upper and left grid can be reached
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
                # do nothing if the value is 1, i.e., an obstacle, as there would be 0 ways to reach there
        return dp[-1][-1]# return the number of ways the last rightmost grid can be reached


