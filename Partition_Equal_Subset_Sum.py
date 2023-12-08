# Title: 416. Partition Equal Subset Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/partition-equal-subset-sum/description

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1: return False
        nums.sort()

        @cache
        def has_combination(target: int, idx: int) -> bool:
            if target == 0:
                return True
            for i in range(idx, len(nums)):
                if nums[i] > target:
                    return False
                elif nums[i] == target:
                    return True
                else:
                    return has_combination(target, idx + 1) or has_combination(target - nums[idx], idx + 1)
        
        return has_combination(total_sum // 2, 0)
