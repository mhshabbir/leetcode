class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Input: grid = [
                        ["1","1","1","1","0"],
                        ["1","1","0","1","0"],
                        ["1","1","0","0","0"],
                        ["0","0","0","0","0"],
                        ]
                        [[1, 0],
                         [1, 0]]
        """
        def dfs(grid, r, c, visited):
            print(r,c)
            if ((r < 0 or c < 0) 
                    or (r == len(grid) or c == len(grid[0]))
                    or grid[r][c] == "0" 
                    or (r,c) in visited):
                visited.add((r,c))
                return
            visited.add((r,c))
            dfs(grid, r+1, c, visited)
            dfs(grid, r-1, c, visited)
            dfs(grid, r, c+1, visited)
            dfs(grid, r, c-1, visited)
        numberOfIsland = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == "1":
                    numberOfIsland += 1
                    dfs(grid, row, col, visited)
        return numberOfIsland
