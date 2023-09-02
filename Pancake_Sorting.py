# Title: 969. Pancake Sorting
# Difficulty: Medium
# Problem: https://leetcode.com/problems/pancake-sorting/description/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def find_max_index(arr, n):
            max_index = 0
            for i in range(1, n):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index

        def reverse(arr, n):
            left, right = 0, n
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        result = []
        for n in range(len(arr), 0, -1):
            max_index = find_max_index(arr, n)
            if max_index != 0:
                reverse(arr, max_index)
                result.append(max_index + 1)
            reverse(arr, n - 1)
            result.append(n)
        
        return result
