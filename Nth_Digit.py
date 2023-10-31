# Title: 400. Nth Digit
# Difficulty: Medium
# Problem: https://leetcode.com/problems/nth-digit/description/

class Solution:
    def findNthDigit(self, n: int) -> int:
        # find n after i-1 digits have passed
        i = 1
        while n - i * 10 ** (i-1) * 9 > 0:
            n -= i * 10 ** (i-1) * 9
            i += 1
        
        # find the i-1th digit greatest interger
        start = int('9' * (i - 1)) if i > 1 else 0
        # find the number
        char = str(start + (n - 1) // i + 1)
        
        # return the digit
        return int(char[(n - 1) % i])
