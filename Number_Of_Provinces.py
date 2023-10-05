class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # initialize required variables
        visited = set()
        graph = defaultdict(list)
        n = len(isConnected)

        # depth_first search
        def dfs(n: int):
            if n not in visited:
                visited.add(n)
                for neighbour in graph[n]:
                    dfs(neighbour)
        
        # create a dictionary of list of neighbours
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # count the number of provinces
        provinces = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces
