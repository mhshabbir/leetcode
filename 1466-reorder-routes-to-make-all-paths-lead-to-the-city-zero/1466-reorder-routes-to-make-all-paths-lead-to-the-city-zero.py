class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = { (a,b) for a,b in connections}
        change = 0
        visited = set()
        neighbor = {i:[] for i in range(n)}
        for a,b in connections:
            neighbor[a].append(b)
            neighbor[b].append(a)

        
        def dfs(city):
            nonlocal change, edges, visited, neighbor
            # city = 0 and nei = 1 and 4
            for nei in neighbor[city]:
                if nei in visited:
                    continue
                if (nei, city) not in edges:
                    change += 1
                visited.add(nei)
                dfs(nei)
            
        
        visited.add(0)
        dfs(0)

        return change

                


