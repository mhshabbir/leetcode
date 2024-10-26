class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROW = len(grid1)
        COL = len(grid1[0])
        grid1island = set()
        visited = set()

        def isIsland(r,c):
            if (r < 0 or r == ROW or c < 0 or c == COL or 
                grid2[r][c] == 0 or 
                (r,c) in visited):
                return True
            visited.add((r,c)) 
            
            res = True
            if grid1[r][c] == 0:
                res = False
            
            res = isIsland(r+1, c) and res
            res = isIsland(r-1, c) and res
            res = isIsland(r, c+1) and res
            res = isIsland(r, c-1) and res

            return res
        
        subIsland = 0
        for r in range(ROW):
            for c in range(COL):
                if grid2[r][c] == 1 and (r,c) not in visited and isIsland(r, c):
                    subIsland += 1

        return subIsland