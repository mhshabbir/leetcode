class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])

        visited = set()

        def checkCycle(node, prev):
            print("working")
            if node in visited:
                return False
            
            visited.add(node)

            for nei in graph[node]:
                if nei == prev:
                    continue
                if not checkCycle(nei, node):
                    print(nei)
                    return False
                
            print((visited))
            return True

        

        return checkCycle(0, -1) and len(visited) == n