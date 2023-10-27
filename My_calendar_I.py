# Title: 729. My Calendar I
# Difficulty: Medium
# Problem: https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.calendar, [start, end])
        if index > 0:
            if self.calendar[index-1][1] > start:
                return False
        if index < len(self.calendar):
            if self.calendar[index][0] < end:
                return False
        self.calendar.insert(index, [start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
