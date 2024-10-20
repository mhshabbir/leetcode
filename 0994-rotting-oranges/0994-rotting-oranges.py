from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        queue.append()
        fresh = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                

        minutes = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                direction = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in direction:
                    newRow, newCol = r+dr, c+dc
                    if (min(newRow, newCol) < 0 or newRow == row or newCol == col or
                        grid[newRow][newCol] != 1):
                        continue
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
                    fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1

