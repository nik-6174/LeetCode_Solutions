# Title: 228. Summary Ranges
# Difficulty: Easy
# Problem: https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        
        intervals, prev = [[nums[0], nums[0]]], nums[0]

        for num in nums[1:]:
            if num != prev + 1:
                intervals[-1] = str(intervals[-1][0]) + "->" + str(prev) if intervals[-1][0] != prev else str(prev)
                intervals.append([num, num])
            prev = num
        intervals[-1] = str(intervals[-1][0]) + "->" + str(prev) if intervals[-1][0] != prev else str(prev)
        
        return intervals
