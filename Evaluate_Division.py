class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Build the graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(node, target, visited):
            if node not in graph:
                return -1.0
            if target in graph[node]:
                return graph[node][target]
            visited.add(node)
            for neighbor, value in graph[node].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return value * result
            return -1.0

        result = []
        for query in queries:
            start, end = query
            visited = set()
            result.append(dfs(start, end, visited))

        return result
