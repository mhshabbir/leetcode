class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # [3,8,-10,23,19,-4,-14,27]
        arr.sort()
        # print(arr)
        
        # [-14, -10, -4, 3, 8, 19, 23, 27]
        resultArr = []
        minAbs = float("inf")
        for left in range(len(arr) - 1):
            if abs(arr[left] - arr[left + 1]) < minAbs:
                minAbs = abs(arr[left] - arr[left + 1])
                resultArr = []
                resultArr.append([arr[left],arr[left + 1]])

            elif abs(arr[left] - arr[left + 1]) == minAbs:
                resultArr.append([arr[left],arr[left + 1]])

        return resultArr