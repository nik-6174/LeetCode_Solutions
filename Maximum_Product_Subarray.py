# Title: 152. Maximum Product Subarray
# Difficulty: Medium
# Probelm: https://leetcode.com/problems/maximum-product-subarray/description

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev = [1, 1]
        max_product = float('-inf')

        for i in range(len(nums)):
            curr_min = min(prev[1] * nums[i], prev[0] * nums[i], nums[i])
            curr_max = max(prev[1] * nums[i], prev[0] * nums[i], nums[i])
            prev = [curr_min, curr_max]
            max_product = max(max_product, curr_max)
        
        return max_product
