# Title: 2125. Number of Laser Beams in a Bank
# Difficulty: Medium
# Problem: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, count = 0, 0

        for i in range(len(bank)):
            temp = bank[i].count('1')
            count += prev * temp
            if temp:
                prev = temp
        
        return count
