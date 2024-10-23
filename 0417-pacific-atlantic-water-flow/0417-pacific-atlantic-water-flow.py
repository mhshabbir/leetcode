class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ROW, COL = len(heights), len(heights[0])
        # pac, atl = set(), set()

        # def dfs(r,c, visit, preHeight):
        #     if ((r,c) in visit 
        #         or r < 0
        #         or c < 0
        #         or r == ROW or c == COL 
        #         or heights[r][c] < preHeight):
        #         return
        #     visit.add((r,c))
        #     direction = [[1,0],[-1,0],[0,1],[0,-1]]
        #     for dr,dc in direction:
        #         dfs(r+dr, c+dc, visit, heights[r][c])

       
        
        # res = []
        # for r in range(ROW):
        #     for c in range(ROW):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])
        # return res
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, preHeight):
            if ((r,c) in visit 
                or r < 0
                or c < 0
                or r == ROWS or c == COLS 
                or heights[r][c] < preHeight):
                return
            visit.add((r,c))
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in direction:
                dfs(r+dr, c+dc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) 

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
