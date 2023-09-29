# Title: 80. Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        shift = 0
        for i in range(2,len(nums)):
            i -= shift
            if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                nums.pop(i)
                shift += 1
        return len(nums)

