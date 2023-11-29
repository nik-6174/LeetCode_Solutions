# Title: 632. Smallest Range Covering Elements from K Lists
# Difficulty: Hard
# Problem: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/

class Solution:
    def smallestRange(self, nums):
        k = len(nums)
        indices = [0] * k
        min_heap = [(nums[i][0], i, 0) for i in range(k)]
        heapq.heapify(min_heap)
        
        min_range = float('-inf'), float('inf')
        max_val = max(nums[i][0] for i in range(k))
        
        while True:
            min_val, list_idx, idx = heapq.heappop(min_heap)
            if max_val - min_val < min_range[1] - min_range[0]:
                min_range = min_val, max_val
            
            indices[list_idx] = idx + 1
            if indices[list_idx] == len(nums[list_idx]):
                break
            
            new_val = nums[list_idx][indices[list_idx]]
            max_val = max(max_val, new_val)
            heapq.heappush(min_heap, (new_val, list_idx, indices[list_idx]))
        
        return list(min_range)
