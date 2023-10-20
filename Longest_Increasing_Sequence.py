# Title: 
# Difficulty: Medium
# Problem: 

# Using Dp with complexity of O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        max_len = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            max_len = max(max_len, dp[i])
        return max_len

## Using unique Approach

class Solution:
    def lengthOfLIS(self, nums):
        subseq = [nums[0]]  # Initialize the subsequence with the first element of the input list.

        for n in nums[1:]:  # Iterate through the remaining elements in the input list.
            i = 0  # Initialize the index to 0 for searching in the subsequence.
            while i < len(subseq) and subseq[i] < n:
                i += 1
            # The while loop finds the position where the current element 'n' should be inserted or updated in the subsequence.
            
            if i >= len(subseq):
                subseq.append(n)  # If 'n' is greater than all elements in the subsequence, add it to the end.
            else:
                subseq[i] = min(subseq[i], n)  # Update the subsequence element at index 'i' with the minimum of its current value and 'n'.

            # The following line is a commented-out print statement for debugging purposes.
            # print(n, subseq)
            
        return len(subseq)  # Return the length of the final LIS.

## With time complexity of O(nlogn) (most efficient)

class Solution:
    def lengthOfLIS(self, nums):
        sub = []  # Initialize an empty list to store the subsequence.

        for num in nums:
            # Find the index at which 'num' should be inserted in 'sub' using binary search.
            idx = self.binarySearchInsertion(sub, num)
            
            if idx == len(sub):
                sub.append(num)  # If 'num' should be inserted at the end of 'sub', simply append it.
            else:
                sub[idx] = num  # If 'num' should replace an existing element in 'sub', update it.

        return len(sub)  # Return the length of the final LIS.

    def binarySearchInsertion(self, sub, num):
        # Manually find the index where 'num' should be inserted into 'sub' using binary search.
        left, right = 0, len(sub) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index.
            
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        return left  # 'left' is the index where 'num' should be inserted.
      
 ## using inbuilt function

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect_left(sub,num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)
            

