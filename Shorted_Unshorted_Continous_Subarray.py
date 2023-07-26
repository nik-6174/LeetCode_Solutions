# Title: 581. Shortest Unsorted Continuous Subarray (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # find the max element and min element in the unsorted array
        min_elem = float('inf')
        max_elem = float('-inf')

        # update the value of max and min
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                min_elem = min(nums[i], min_elem)
                max_elem = max(nums[i-1], max_elem)

        # in case the array is already sorted
        if max_elem == float('-inf'):
            return 0
        
        # we find the starting and ending indexes of shorted array
        idx1, idx2 = -1, -1

        for i in range(len(nums)):
            if nums[i] > min_elem:
                idx1 = i
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_elem:
                idx2 = i
                break
        
        # return the length of unsorted array as ending index - starting index + 1
        return idx2 - idx1 + 1

