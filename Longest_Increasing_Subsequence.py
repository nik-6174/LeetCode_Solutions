# Title: 300. Longest Increasing Subsequence
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-increasing-subsequence/description/

## Using Dynamic Programming: O (n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        max_len = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            max_len = max(max_len, dp[i])
        return max_len


## Using Binary Search and Lists: O (n logn)
class Solution:
    def lengthOfLIS(self, nums):
        sub = [nums[0]]  # Initialize an empty list to store the subsequence.

        for num in nums[1:]:
            # Find the index at which 'num' should be inserted in 'sub' using binary search.
            if num > sub[-1]:
                sub.append(num) # If 'num' should be inserted at the end of 'sub', simply append it.
            else:
                idx = bisect.bisect_left(sub, num)
                # idx = self.binarySearchInsertion(sub, num)
                sub[idx] = num  # If 'num' should replace an existing element in 'sub', update it.
        return len(sub)  # Return the length of the final LIS.
    
    '''
    Use this manual binary search, or use bisect_left from bisect library
    # bisect_left is more optimized
    
    def binarySearchInsertion(self, sub, num):
        # Manually find the index where 'num' should be inserted into 'sub' using binary search.
        left, right = 0, len(sub) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index.
            
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        return left  # 'left' is the index where 'num' should be inserted.
    '''
