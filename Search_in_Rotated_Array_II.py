# Title: 81. Search in Rotated Sorted Array II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] == nums[start]:
                start += 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
