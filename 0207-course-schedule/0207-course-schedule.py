from collections import deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
                0 -> 1
                     ^
        """
        # courseMap = defaultdict(list)
        # visited = set()

        # for preReq in prerequisites:
        #     courseMap[preReq[1]].append(preReq[0])

        # if not prerequisites:
        #     return True
        # queue = deque()
        # queue.append(prerequisites[0][1])

        # while queue:
        #     for i in range(len(queue)):
        #         cur = queue.popleft()
        #         visited.add(cur)
            
        #     for neighbor in courseMap[cur]:
        #         if neighbor in visited:
        #             return False
        #         else:
        #             queue.append(neighbor)
            
        # return True if len(visited) == numCourses else False
        
        courseMap = defaultdict(list)
        visited = set()

        for preReq in prerequisites:
            courseMap[preReq[1]].append(preReq[0])
        
        def dfs(course):
            if course in visited:
                return False
            if courseMap[course] == []:
                return True

            visited.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            courseMap[course] = []
            return True
            
        for course in courseMap.keys():
            if not dfs(course): return False
        return True
        


