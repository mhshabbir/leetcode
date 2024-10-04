class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
                        M              R                            
                       V      v               
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
                    ^          
             L
        """
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (right+left)//2
            innerLeft = 0
            innerRight = len(matrix[mid]) - 1
            while innerLeft <= innerRight:
                innerMid = (innerLeft + innerRight)//2
                if target >= matrix[mid][innerLeft] and target <= matrix[mid][innerRight]:
                    if target < matrix[mid][innerMid]:
                        innerRight = innerMid - 1
                    elif target > matrix[mid][innerMid]:
                        innerLeft = innerMid + 1
                    else:
                        return True
                elif target < matrix[mid][innerLeft]:
                    right = mid - 1
                    break
                elif target > matrix[mid][innerRight]:
                    left = mid + 1
                    break
        return False
                    
                    
            