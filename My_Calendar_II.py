# Title: 731. My Calendar II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/my-calendar-ii/description/


class MyCalendarTwo:

    def __init__(self):
        self.calendar = set()
        self.double_bookings = set()

    def book(self, start: int, end: int) -> bool:
        # Check for double bookings
        for s, e in self.double_bookings:
            if start < e and end > s:
                return False

        # Check for overlaps with previous bookings
        for s, e in self.calendar:
            if start < e and end > s:
                self.double_bookings.add((max(s, start), min(e, end)))

        self.calendar.add((start, end))
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
