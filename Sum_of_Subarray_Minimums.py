# TItle: 907. Sum of Subarray Minimums
# Difficulty: Medium
# Problem: https://leetcode.com/problems/sum-of-subarray-minimums/description/

# Using monotonic stack ( High Efficiency : Complexity : O(n) | O(n) )
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, res = [], 0

        # maintain an increasing monotonic stack
        for idx, val in enumerate(arr + [-1]):
            while stack and stack[-1][1] >= val: # pop when next element is smaller
                pivot, min_val = stack.pop()
                right = idx - pivot # find the length of max subarray to the right
                # find the length of max subarray to the left
                if stack:
                    left = pivot - stack[-1][0]
                else:
                    left = pivot + 1
                # add the number of subarrays with minimum as min_val
                res += left * right * min_val
                res %= 10**9 + 7 # find modulo
            stack.append([idx, val])
        
        return res

# Using binary search ( Low efficiency : Complexity: O(nlogn) | O(n) )
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        seen, res, modulo = [-1, len(arr)], 0, 10**9 + 7

        indexes = list(range(len(arr)))
        indexes.sort(key=lambda x: arr[x])

        for i in range(len(arr)):
            idx = bisect.bisect_left(seen, indexes[i])
            left = indexes[i] - seen[idx-1]
            right = seen[idx] - indexes[i]
            seen.insert(idx, indexes[i])
            res += left * right * arr[indexes[i]]
            res = res % modulo
        return res
