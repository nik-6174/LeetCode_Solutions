# Title: 875. Koko Eating Bananas
# Difficulty: Medium
# Problem: https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # trivial case
        if h == len(piles): return max(piles)
        
        start, end = 1, max(piles)
        ans = float('inf')
        while start < end:
            mid = (start + end) // 2
            if sum(map(lambda x:ceil(x/mid),piles)) > h:
                start = mid + 1
            else:
                ans = min(ans, mid)
                end = mid
        return ans if ans != float('inf') else end
