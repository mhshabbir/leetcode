class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            0 -> 1,2
            1 -> []
            2 -> 3
            3 -> []
        """
        courseMap = defaultdict(list)
        pathway = set()

        for preReq in prerequisites:
            courseMap[preReq[1]].append(preReq[0])

        def dfs(course):
            if course in pathway:
                return False
            if courseMap[course] == []:
                return True
            pathway.add(course)
            for prereqs in courseMap[course]:
                if not dfs(prereqs):
                    return False
            courseMap[course] = []
            pathway.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True 