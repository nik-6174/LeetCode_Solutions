# Title: 
# Difficulty: Medium
# Problem: 

# Using Loop ##
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if(n % 2 == 0): n /= 2
            elif((n - 1)/2 % 2 == 0 or (n-1)/2 == 1): n -= 1
            elif((n + 1)/2 % 2 == 0): n += 1
            else: n -= 1
            count += 1
        return count

# Using Recurrsion
class Solution:
    def integerReplacement(self, n: int) -> int:
        # when n is even
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))
