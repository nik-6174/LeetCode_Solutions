# Title: 54. Spiral Matrix
# Difficulty: Medium
# Problem: https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total_elements = len(matrix) * len(matrix[0])
        visited = set()
        seq = []
        curr = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        dir_index = 0
        
        for _ in range(total_elements):
            seq.append(matrix[curr[0]][curr[1]])
            visited.add((curr[0], curr[1]))
            
            next_row, next_col = curr[0] + directions[dir_index][0], curr[1] + directions[dir_index][1]
            
            if (
                next_row < 0 or next_row >= len(matrix) or
                next_col < 0 or next_col >= len(matrix[0]) or
                (next_row, next_col) in visited
            ):
                # Change direction
                dir_index = (dir_index + 1) % 4  # Cycle through directions (0, 1, 2, 3)
                next_row, next_col = curr[0] + directions[dir_index][0], curr[1] + directions[dir_index][1]
                
            curr[0], curr[1] = next_row, next_col

        return seq
