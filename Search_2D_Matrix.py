class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # assume the matrix as a 1D array in row major
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right)//2
            # find the corresponding coordinated in 2d matrix
            x, y = mid % n, mid // n
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
