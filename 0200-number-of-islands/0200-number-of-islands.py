class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or 
            (row, col) in visited or grid[row][col] == "0"):
                return
            
            visited.add((row,col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # def bfs(r,c):
        #     q = collections.deque()
        #     visited.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(ROWS) and c in range(COLS) and (r,c) not in visited and grid[r][c] == "1"):
        #                 q.append((r,c))
        #                 visited.add((r,c))


        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count += 1

        return count