# Title: 945. Minimum Increment to Make Array Unique (LeetCode)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # create a set of all unique numbers
        visited = set()

        # create a list to append all numbers that have to be moved
        extra = []
        for num in nums:
            if num in visited:
                extra.append(num)
            else:
                visited.add(num)
        
        # sort extra
        extra.sort()

        # return 0 if already all numbers are unique
        if not extra:
            return 0
        
        # start from the minimum element in extra
        i = extra[0]

        # find new values for each element in extra and store the difference in old and new value
        j = 0
        ans = 0

        while j < len(extra):
            if extra[j] > i:
                i = extra[j] # start from next value in extra
            elif i not in visited:
                ans += (i - extra[j]) # add the number of moves required to make the number unique
                j += 1
            i += 1
        
        return ans

