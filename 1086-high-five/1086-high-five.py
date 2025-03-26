class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        result = []
        for item in items:
            id, score = item
            scores[id].append(score)
        
        for id in scores.keys():
            allScores = sorted(scores[id], reverse=True)
            topFive = allScores[:5]
            print(topFive)
            averageScore = sum(topFive)//5
            result.append([id, averageScore])
        
        result.sort(key = lambda x: x[0])
        
        return result