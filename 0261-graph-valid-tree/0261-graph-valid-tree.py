class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a graph is a tree if it has no cycles
        # so basically traverse and look for cycles
        if not edges and n < 2:
            return True

        adjList = {}
        for a, b in edges:
            adjList[a] = adjList.get(a, []) + [b]
            adjList[b] = adjList.get(b, []) + [a]
        def dfs(vertex, parent, visited):
            if vertex in visited:
                return False
            
            visited.add(vertex)
            if not adjList.get(vertex):
                return False

            for nei in adjList[vertex]:
                if nei == parent:
                    continue
                if not dfs(nei, vertex, visited):
                    return False
            return True
        visited = set()
        res = dfs(0, None, visited)
        return res and len(list(visited)) == n