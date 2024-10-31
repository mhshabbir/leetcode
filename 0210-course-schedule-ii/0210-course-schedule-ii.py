class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # pathway = set()
        # result = []
        # courseMap = {c: [] for c in range(numCourses)}
        # for crs, pre in prerequisites:
        #     courseMap[crs].append(pre)

        # def dfs(course):
        #     if course in pathway:
        #         return False
        #     if course == []:
        #         return True
            
        #     pathway.add(course)
        #     for prereq in courseMap[course]:
        #         if not dfs(course): False
            
        #     pathway.remove(course)
        #     courseMap[course] = []
        #     result.append(course)
        #     return True

        # for course in range(numCourses):
        #     if not dfs(course): return []
        # return result
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        