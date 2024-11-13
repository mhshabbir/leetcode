class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # output the top row
            for i in range(left, right):
                output.append(matrix[left][i])
            top += 1

            # output the right column 
            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right):
                break
            
            # output the last row
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom -1][i])
            bottom -= 1

            # output the left column
            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        return output
