

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        cycle = set()
        visit = set()
        output = []
        courseMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
        

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in courseMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

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

        for course in range(numCourses):
            if not dfs(course): return []
        return output

        