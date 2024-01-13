# Title: 85. Maximal Rectangle
# Difficulty: Hard
# Problem: https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0])+1)
        max_area = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # find the biggest rectangle in the histogram
            stack = []

            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1 if stack else i
                    max_area = max(max_area, width * height)
                stack.append(i)
        return max_area
