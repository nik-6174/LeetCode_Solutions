# Title: 435. Non-overlapping Intervals
# Difficulty: Medium
# Problem: https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] >= last_interval[1]:
                last_interval = interval
            elif interval[1] < last_interval[1]:
                last_interval = interval
                count += 1
            else:
                count += 1
                continue
        return count
