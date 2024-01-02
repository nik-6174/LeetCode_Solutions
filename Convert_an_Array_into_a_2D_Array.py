# TItle: 2610. Convert an Array Into a 2D Array With Conditions
# Difficulty: Medium
# Problem: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans, counter = [], {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

            if counter[num] > len(ans):
                ans.append([])
            
            ans[counter[num]-1].append(num)
        return ans
