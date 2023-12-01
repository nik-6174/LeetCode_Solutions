# Title: 264. Ugly Number II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/ugly-number-ii/description/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1

        i2, i3, i5 = 0, 0, 0
        next_ugly_number = 1

        for i in range(1, n):
            next_ugly_number = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
            ugly_numbers[i] = next_ugly_number

            if next_ugly_number == ugly_numbers[i2] * 2: i2 += 1 
            if next_ugly_number == ugly_numbers[i3] * 3: i3 += 1
            if next_ugly_number == ugly_numbers[i5] * 5: i5 += 1
        
        return next_ugly_number
