from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        row, col = len(grid), len(grid[0])
        if not grid or grid[0][0] == 1 or grid[row-1][col-1]:
            return -1
        queue = deque()
        visited = set()
        queue.append((0,0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                # print("initial", r, c)
                directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc
                    # print(newRow, newCol)
                    if (min(newRow, newCol) < 0 or newRow == row or newCol == col or
                        grid[newRow][newCol] == 1 or (newRow, newCol) in visited):
                        # print("err", newRow, newCol)
                        continue
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
                if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
                    return length
            length += 1
        
        return -1
        


