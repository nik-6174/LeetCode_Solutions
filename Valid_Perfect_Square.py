# Title: 367. Valid Perfect Square
# Difficulty: Easy
# Problem: https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        start, end = 0, num // 2

        while start <= end:
            mid = (start + end) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
