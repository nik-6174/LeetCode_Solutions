# Title: 1466. Reorder Routes to Make All Paths Lead to the City Zero
# Difficulty: Medium
# Problem: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        change_count = 0
        
        for u, v in connections:
            graph[u].append((v, 1))  # Edge from u to v (forward)
            graph[v].append((u, -1))  # Edge from v to u (backward)
        
        visited = set()
        
        def dfs(node):
            nonlocal change_count
            visited.add(node)
            
            for neighbor, direction in graph[node]:
                if neighbor not in visited:
                    change_count += direction == 1  # Count edges that need to be changed
                    dfs(neighbor)
        
        dfs(0)  # Start DFS traversal from city 0
        
        return change_count
