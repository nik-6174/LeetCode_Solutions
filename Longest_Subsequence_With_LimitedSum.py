# Title: 2389. Longest Subsequence With Limited Sum
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort the input list 'nums' in ascending order.
        nums.sort()

        # Create an empty list to store the results.
        res = []

        # Calculate cumulative sums of 'nums' for efficient query processing.
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        # Process each query in 'queries'.
        for query in queries:
            if query < nums[0]:
                # If the query is less than or equal to the smallest element in 'nums',
                # there are no elements in 'nums' that are less than or equal to the query.
                res.append(0)
            elif query >= nums[-1]:
                # If the query is greater than or equal to the largest element in 'nums',
                # all elements in 'nums' are less than or equal to the query.
                res.append(len(nums))
            else:
                # Perform binary search to find the rightmost index where 'query' can be inserted
                # while maintaining the sorted order. This index represents the count of elements
                # less than or equal to the query.
                start, end = 0, len(nums) - 1
                while start < end:
                    mid = (start + end) // 2
                    if nums[mid] <= query:
                        start = mid + 1  # Move to the right half.
                    else:
                        end = mid  # Move to the left half.
                res.append(start)
        return res

        
