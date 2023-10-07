# Title: 901. Online Stock Span
# Difficulty: Medium
# Problem: https://leetcode.com/problems/online-stock-span/description/


class StockSpanner:

    def __init__(self):
        # stack holds (price, span) decreasing
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
