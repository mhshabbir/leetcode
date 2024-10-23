from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # def dfs(r,c):
        #     if (min(r

        #     if rooms[row][col] == -1:
        #         return 0
        #     if rooms[row][col] == 0:
        #         return 
            
        #     dfs(row+1, col)
        #     dfs(row-1, col)
        #     dfs(row, col+1)
        #     dfs(row, col-1)

        #     return count + 1
        # for row in range(len(rooms)):
        #     for col in range(len(rooms[0])):
        #         if rooms[row][col] == 2147483647:
        #             rooms[row][col] = dfs(row,col)
        ROW = len(rooms)
        COL = len(rooms[0])
        queue = deque()
        visited = set()

        def addRoom(r,c):
            if (r < 0 or r == ROW or c < 0 or c == COL
            or (r,c) in visited or rooms[r][c] == -1):
                return 
            visited.add((r,c))
            queue.append((r,c))

        for row in range(ROW):
            for col in range(COL):
                if rooms[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()       
                rooms[r][c] = distance
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            distance += 1

