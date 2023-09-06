# Title: 134. Gas Station
# Difficulty: Medium
# Problem: https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        # subtract the cost from the gas
        for i in range(n):
            gas[i] -= cost[i]
        
        # find the cummulative gas value
        for i in range(1,n):
            gas[i] += gas[i-1]

        # if there is no possible way make a round trip
        if gas[-1] < 0:
            return -1
        
        # find the min
        min_val = min(gas)

        # find the min index of min_value
        res = gas.index(min_val) + 1

        # when the last value is minimum, we take the 0th index
        if gas[-1] == min_val:
            res = 0
        return res
