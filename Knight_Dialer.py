# Title: 935. Knight Dialer
# Difficulty: Medium
# Problem: https://leetcode.com/problems/knight-dialer/description

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10

        @functools.cache
        def dfs(coordinate, depth):
            if coordinate == (1, 1): return 0 # number 5 has no knight jumps
            if depth == 1: return len(graph[coordinate])
            return sum([dfs(coor, depth-1) for coor in graph[coordinate]]) % (10**9 + 7)

        
        # make a graph for knight moves
        graph = {
            (0, 1): [(2, 0), (2, 2)],
            (1, 2): [(0, 0), (3, 1), (2, 0)],
            (2, 1): [(0, 0), (0, 2)],
            (0, 0): [(1, 2), (2, 1)],
            (3, 1): [(1, 2), (1, 0)],
            (1, 1): [],
            (2, 0): [(0, 1), (1, 2)],
            (0, 2): [(2, 1), (1, 0)],
            (2, 2): [(0, 1), (1, 0)],
            (1, 0): [(3, 1), (0, 2), (2, 2)]
        }
        coordinates = {(0, 1), (1, 2), (2, 1), (0, 0), (3, 1), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}

        return sum([dfs(coordinate, n-1) for coordinate in coordinates]) % (10**9 + 7)
