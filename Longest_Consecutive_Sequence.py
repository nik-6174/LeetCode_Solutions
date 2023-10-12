# TItle: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # create all required vaiables
        max_len, nums_set,  heads = 1, set(nums), set()
        
        # fill the heads set with values of all possible head of longest consecutive sequence
        for num in nums:
            if num - 1 not in nums_set:
                heads.add(num)

        # check the maximum length of each sequence
        for head in heads:
            temp = head

            # check if next consecutive number is in the nums set
            while temp + 1 in nums_set:
                temp = temp + 1
            
            # update the maximum length of sequence
            max_len = max(max_len, temp - head + 1)
        
        return max_len
