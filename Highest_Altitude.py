# Title: 1732. Find the Highest Altitude (LeetCode)
# Difficulty: Easy
# Problem: https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
      # for starting from the 0 altitude insert
        gain.insert(0, 0)
        max_altitude = 0
        for i in range(1, len(gain)): # calculate the cumulative altitude (absolute altitude)
            gain[i] += gain[i-1]
            max_altitude = max(max_altitude, gain[i]) # update max
        return max_altitude
