# Title: 209. Minimum Size Subarray Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/description/

## Optimal solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        min_len = float('Inf')
        windowSum = 0

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                min_len = min(min_len, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1
        
        if min_len == float('Inf'):
            return 0
        
        return min_len

## General Approach Solution using binary search
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # define a function to check if the subarray of given length has max sum >= target
        def check(length: int) -> bool:
            curr_sum = sum(nums[:length])
            if curr_sum >= target:
                return True
            for i in range(length, len(nums)):
                curr_sum += (nums[i] - nums[i-length])
                if curr_sum >= target:
                    return True
            return False
        # find the min size of subarray
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if check(mid):
                if not check(mid-1): # when we need at least mid length subarray
                    return mid
                end = mid-1
            else:
                if check(mid+1):
                    return mid+1
                start = mid+1
        return 0
