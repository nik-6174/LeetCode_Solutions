# TItle: 373. Find K Pairs with Smallest Sums
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap, res = [], []

        for i in range(min(k, len(nums1))):
            # Add pairs with the first element from nums1 and the corresponding index
            # from nums2, along with the sum of the pair to a min-heap.
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and heap:
            # Pop the smallest sum pair from the heap.
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                # If there are more elements in nums2, add the next pair with nums1[i]
                # and nums2[j+1] to the heap.
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1

        return res
