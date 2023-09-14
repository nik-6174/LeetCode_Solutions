# Title: 162. Find Peak Element
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
