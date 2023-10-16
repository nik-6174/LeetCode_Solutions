# Title: 1318. Minimum Flips to Make a OR b Equal to c
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

## Using Strings

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A = bin(a)[2:]
        B = bin(b)[2:]
        C = bin(c)[2:]

        # padd the numbers to be of the same length
        max_len, res = max(len(A), len(B), len(C)), 0
        A = (max_len - len(A)) * '0' + A
        B = (max_len - len(B)) * '0' + B
        C = (max_len - len(C)) * '0' + C

        for i in range(max_len):
            if A[i] == '0' and B[i] == '0':
                if C[i] == '1':
                    res += 1
            elif A[i] == '1' and B[i] == '1':
                if C[i] == '0':
                    res += 2
            else:
                if C[i] == '0':
                    res += 1
        return res

  ## Using Bit Manipulation

  class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            a_right = a & 1
            b_right = b & 1
            c_right = c & 1
            if c_right == 0:
                flips += a_right + b_right
            elif c_right:
                flips += not (a_right or b_right)
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return flips
