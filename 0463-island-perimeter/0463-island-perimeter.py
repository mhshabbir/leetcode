class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        perimeter = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        r = dr + row
                        c = dc + col
                        if (r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0):
                            perimeter += 1
        return perimeter
