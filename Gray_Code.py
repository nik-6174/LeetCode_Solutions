# Title: 89. Gray Code (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/gray-code/description/

# using xor (^) directly
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []

        # find the gray code for first 2**n whole numbers
        for i in range(2**n):
            result.append(i ^ (i >> 1)) # perform bitwise xor between i and i >> 1
        return result

# using xor function
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # we find the xor of two given str bits
        def xor(bit1: str, bit2: str) -> str:
            if bit1 == bit2:
                return '0'
            else:
                return '1'
        
        # storing the integer for gray code
        res = []

        for i in range(2**n):
            binary = bin(i)[2:] # find the binary
            gray = binary[0] # most significant bit is same
            for i in range(len(binary)-1):
                gray += xor(binary[i], binary[i+1]) # we take xor of two consecutive bits
            res.append(int(gray, 2)) # we convert from binary to int
        
        return res
