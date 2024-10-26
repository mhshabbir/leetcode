class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r == len(grid) or
                c == len(grid[0]) or
                grid[r][c] == 0):
                return 1
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))

            return (dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
            
        
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)
                    return perimeter

        
        
        # R = len(grid)
        # C = len(grid[0])

        # perimeter = 0
        # for row in range(R):
        #     for col in range(C):
        #         if grid[row][col] == 1:
        #             directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #             for dr, dc in directions:
        #                 r = dr + row
        #                 c = dc + col
        #                 if (r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0):
        #                     perimeter += 1
        # return perimeter
