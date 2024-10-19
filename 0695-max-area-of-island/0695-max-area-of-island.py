class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == len(grid) or 
                c == len(grid[0]) or
                (r,c) in visited or
                grid[r][c] == 0):
                return 0
            visited.add((r,c))
            # a = dfs(r + 1, c)
            # b = dfs(r - 1, c)
            # c = dfs(r, c + 1)
            # d = dfs(r, c - 1)
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)) 

        maxArea = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if grid[row][col] == 1 and (row,col) not in visited:
                maxArea = max(dfs(row, col), maxArea)
        return maxArea

        