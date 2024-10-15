import collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pairMapping = defaultdict(list) 
        minElement = 0
        for pair in adjacentPairs:
            pairMapping[pair[0]].append(pair[1])
            pairMapping[pair[1]].append(pair[0])
       # {-2:{4}, 4{-2, 1}, 1{4, -3}, -3{1}}
        
        res = []
        for key in pairMapping.keys():
            if len(pairMapping[key]) == 1:
                res.append(key)
                res.append(pairMapping[key][0])
                break
        #{-2, 4, }
        while len(res) < len(adjacentPairs) + 1:
            key = res[-1]
            if len(pairMapping[key]) == 1 and pairMapping[key][0] not in res:
                res.append(pairMapping[key][0])
            if len(pairMapping[key]) == 2:
                if pairMapping[key][0] not in res:
                    res.append(pairMapping[key][0])
                if pairMapping[key][1] not in res:
                    res.append(pairMapping[key][1])
        return res
    
            
