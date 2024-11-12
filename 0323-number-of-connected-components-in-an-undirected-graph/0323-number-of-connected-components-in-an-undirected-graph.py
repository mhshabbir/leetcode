class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = 0
        visited = set()
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def visitNode(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                visitNode(nei)
            
        for node in range(n):
            if node not in visited:
                count += 1
                visitNode(node)

        return count