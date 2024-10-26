class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        """
        1->3 
        2->3
        3->1

        find a key that trust nobody
        make sure that key is in all the others
        """
        judgeSet = set()
        trustMap = defaultdict(list)
        for a, b in trust:
            trustMap[a].append(b)
            judgeSet.add(b)
        
        # for a in trustMap.keys():
        #     if a in judgeSet:
        #         judgeSet.remove(a)


        if len(judgeSet) != 1:
            return -1
        else:
            return judgeSet.pop()


        