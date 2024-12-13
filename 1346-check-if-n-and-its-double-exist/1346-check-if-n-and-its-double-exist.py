class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_map = {}
        for index, arr_element in enumerate(arr):
            arr_map[arr_element] = index
        
        for index, arr_element in enumerate(arr):
            if 2*arr_element in arr_map and arr_map[2*arr_element] != index:
                return True
        return False
