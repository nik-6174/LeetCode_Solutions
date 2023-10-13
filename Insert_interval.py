# Ttile: 57. Insert Interval
# Difficulty: Medium
# Problem: https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        # add a dummy interval
        intervals.append([float('inf'), float('inf')])

        n = len(intervals)

        start, end = -1, -1

        # insert the new interval
        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                end = i
                break
            elif intervals[i][1] < newInterval[0]:
                continue
            else:
                if start == -1:
                    start = i
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # pop the end
        intervals.pop()

        if start == -1:
            start = end
        
        return intervals[:start] + [newInterval] + intervals[end:]
