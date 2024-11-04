class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        result = 0
        visited = set()
        LIP = {}

        def dfs(row, col, prev_cell):
            if (row < 0 or col < 0 or row == ROWS or col == COLS
                or (row,col) in visited or matrix[row][col] <= prev_cell):
                return 0
            if (row, col) in LIP:
                return LIP[(row,col)]
            
            visited.add((row, col))

            res1 = dfs(row+1, col, matrix[row][col])
            res2 = dfs(row-1, col, matrix[row][col])
            res3 = dfs(row, col+1, matrix[row][col])
            res4 = dfs(row, col-1, matrix[row][col])

            longest = max(1 + res1, 1 + res2, 1 + res3, 1 + res4)
            visited.remove((row, col))
            LIP[(row,col)] = longest
            
            return longest

        for row in range(ROWS):
            for col in range(COLS):
                result = max(result, dfs(row, col, -1))

        return result