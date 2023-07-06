# Title: 1679. Max Number of K-Sum Pairs (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # create a dict
        d = Counter(nums)
        # d = defaultdict(int)
        # for i in nums:
        #    d[i] += 1

        # init a counter
        count = 0
        for i in d:
            while d[i] and k-i in d: # check if k-i exists in dictonary
                d[i] -= 1 # decrement the number of i items in d
                if d[k-i]: # check if the number of k-i items in d is more than 0
                    count += 1
                    d[k-i] -= 1 # decrement the number of k-i items since we removed it from d
                else:
                    break
        return count
