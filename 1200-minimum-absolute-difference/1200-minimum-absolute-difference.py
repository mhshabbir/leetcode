class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        output = []
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < minDiff:
                output = []
                minDiff = abs(arr[i] - arr[i + 1]) 
                output.append([arr[i], arr[i + 1]])
            elif abs(arr[i] - arr[i+1]) == minDiff:
                output.append([arr[i], arr[i+1]])

        return output