class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            0 -> 1,2
            1 -> []
            2 -> 3
            3 -> []
        """
        courseMap = defaultdict(list)
        # for pre, crs in prerequisites:
        #     courseMap[crs].append(pre)
        for preReq in prerequisites:
            courseMap[preReq[1]].append(preReq[0])
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if courseMap[course] == []:
                return True
            
            cycle.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            courseMap[course] = []
            cycle.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
