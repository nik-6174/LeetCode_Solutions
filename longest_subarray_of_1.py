# Title: 1493. Longest Subarray of 1's After Deleting One Element (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      # when there is no 0 in nums, we should delete a 1 and return the sum
        if 0 not in nums:
            return sum(nums) - 1
        sums = []
        cumsum = 0
        nums.append(0) # so that the last iteration in loop appends the sum for the last continous sequence of 1s
        for i in nums:
            if i == 0:
                sums.append(cumsum) # append the sum of continous 1s so far
                sums.append(0) # add a 0
                cumsum = 0 # reinitialize the cumulative sum
            else:
                cumsum += i # add the cumulative values
        max_sum = 0
      # since the list has to be alternating 0s and number of continous 1s, we can sum 3 consecutive values
      # which would be either num, 0, num' or it would be 0, num, 0
      # both the cases are valid
        for i in range(len(sums)):
            if i < len(sums)-2: # check if the sum of 3 consecutive elements of alternating numbers and 0 is greater than max_sum seen so far
                max_sum = max(max_sum, sums[i] + sums[i+1] + sums[i+2]) # in case it is, change the value
        return max_sum
