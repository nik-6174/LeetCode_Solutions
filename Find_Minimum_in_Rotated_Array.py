# Title: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[end] < nums[mid]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
