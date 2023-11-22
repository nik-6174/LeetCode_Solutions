# Title: 918. Maximum Sum Circular Subarray
# Difficulty: Medium
# Problem: https://leetcode.com/problems/maximum-sum-circular-subarray/description

class Solution:
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        
        max_ending_here_max = nums[0]
        max_so_far_max = nums[0]
        min_ending_here_min = nums[0]
        min_so_far_min = nums[0]
        total_sum = nums[0]
        
        for i in range(1, n):
            max_ending_here_max = max(nums[i], max_ending_here_max + nums[i])
            max_so_far_max = max(max_so_far_max, max_ending_here_max)
            
            min_ending_here_min = min(nums[i], min_ending_here_min + nums[i])
            min_so_far_min = min(min_so_far_min, min_ending_here_min)
            
            total_sum += nums[i]
        
        if total_sum == min_so_far_min:
            return max_so_far_max
        
        return max(max_so_far_max, total_sum - min_so_far_min)
