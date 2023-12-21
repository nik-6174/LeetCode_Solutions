# Title: 201. Bitwise AND of Numbers Range
# Difficulty: Medium
# Problem: https://leetcode.com/problems/bitwise-and-of-numbers-range/description

# Using strings
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        binaries = [bin(right)[2:], bin(left)[2:]]
        k1, k2 = map(len, binaries)
        # when there is a difference in the value of k1 & k2 -> it will be zero
        if k1 != k2:
            return 0
        else:
            for i in range(k1):
                if binaries[0][i] != binaries[1][i]:
                    return int(binaries[0][:i] + "0" * (k1 - i), 2)
            return right

# Using Bit operations (more efficient)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common leftmost bits
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Shift back to the left to get the final result
        return left << shift
