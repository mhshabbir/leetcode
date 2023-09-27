class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        #    L^                 ^M            ^R
        
        # [[1,3,5,7],[10,11,16,20]]
        #  L^      ^M           ^R

        # [1,3,5,7]
        #  L^ M   R

        # for row in matrix:
        left = 0
        ileft = 0
        right = len(matrix)-1
        iright = len(matrix[right])-1

    
        # print(matrix[left][iLeft]) 
        # print(matrix[right][iRight])    
        # print(matrix[mid][iMid]) 
        

        while left <= right:
            mid=(left+right)//2
            if target >= matrix[mid][ileft] and target <= matrix[mid][iright]:
                while ileft <= iright:
                    imid=(ileft + iright)//2
                    if matrix[mid][imid] == target:
                        return True
                    elif target > matrix[mid][imid]:
                        ileft = imid + 1
                    elif target < matrix[mid][imid]:
                        iright = imid -1
            elif target < matrix[mid][ileft]:
                right = mid - 1
            elif target > matrix[mid][iright]:
                left = mid + 1
        return False
            