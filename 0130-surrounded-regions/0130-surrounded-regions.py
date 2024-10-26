class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if (c < 0 or r < 0 or c == COLS or r == ROWS or board[r][c] != "O" or (r,c) in visited):
                return 
            
            visited.add((r,c))

            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in direction:
                dfs(r+dr, c+dc)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [0, COLS - 1]):
                    dfs(row,col)
        print(visited)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row,col) not in visited:
                    board[row][col] = "X"
                
                    