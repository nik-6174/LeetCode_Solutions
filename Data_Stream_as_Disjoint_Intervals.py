# Title: 352. Data Stream as Disjoint Intervals
# Difficulty: Hard
# Problem: https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/

class SummaryRanges:

    def __init__(self):
        self.intervals = []
        

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals = [[value, value]]
            return

        n = len(self.intervals)

        # find the index where we need to put the interval [value, value] in the intervals
        index = bisect.bisect_left(self.intervals, [value, value])
        
        # when value merges previous and the next intervals
        if index != len(self.intervals) and index != 0 and self.intervals[index-1][1]+1 == value and value == self.intervals[index][0]-1:
            self.intervals[index-1][1] = self.intervals[index][1]
            self.intervals.pop(index)
            return
        
        if index > 0:
            # when value lies in previous interval
            if self.intervals[index-1][0] <= value <= self.intervals[index-1][1]:
                return
            # when value extends previous interval
            if value == self.intervals[index-1][1] + 1:
                self.intervals[index-1][1] += 1
                return
        
        if index < len(self.intervals):
            # when value lies in next interval
            if self.intervals[index][0] <= value <= self.intervals[index][1]:
                return
            # when value extends next interval
            if self.intervals[index][0] == value + 1:
                self.intervals[index][0] = value
                return
        
        # if value neither extends not merges next and previous interval
        self.intervals.insert(index, [value, value])


    def getIntervals(self) -> List[List[int]]:
        return self.intervals
   


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
