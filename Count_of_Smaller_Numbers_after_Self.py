# Title: 315. Count of Smaller Numbers After Self
# Difficulty: Hard
# Problem: https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

import array
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = array.array('h')  # List to maintain the sorted elements encountered so far
        result = [0] * len(nums)      # List to store the count of smaller elements

        for idx in range(len(nums)-1, -1, -1):
            # Find the index where num should be inserted to maintain sorted order
            index = bisect.bisect_left(sorted_nums, nums[idx])
            # update the index to the result
            result[idx] = index
            # Insert num at the appropriate position in sorted_nums
            sorted_nums.insert(index, nums[idx])

        return result
