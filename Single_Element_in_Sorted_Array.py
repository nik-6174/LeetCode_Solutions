# Title: 540. Single Element in a Sorted Array
# Difficulty: Medium
# Problem: https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == nums[mid-1]:
                if mid % 2 == 0:
                    end = mid - 2
                else:
                    start = mid + 1
            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
            else:
                return nums[mid]
        return nums[start]
