# Title: 2483. Minimum Penalty for a Shop
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # count the panelty on closing the shop at 0th hour
        penalty = customers.count('Y')
        min_hour = [0, penalty]
        for i in range(len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_hour[1]:
                min_hour = [i+1, penalty]
        return min_hour[0]
            
