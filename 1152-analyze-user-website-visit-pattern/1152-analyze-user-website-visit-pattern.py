from itertools import combinations
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        for t, user, site in sorted(zip(timestamp, username, website)):
            graph[user].append(site)
        
        scores = defaultdict(int)
        for user, site in graph.items():
            for pattern in set(combinations(site, 3)):
                scores[pattern] += 1

        print(scores)
        max_score_arr = []
        for pattern, score in scores.items():
            max_score_arr.append(((score * -1), pattern))
        
        heapq.heapify(max_score_arr)
        return heapq.heappop(max_score_arr)[1]