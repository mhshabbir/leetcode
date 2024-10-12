class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        for loop [3]

        
        
        
        """
        if rowIndex == 0:
            return [1]
        row = [1,1] 
                    #    [1   3]
                    #    [1,1] 
        for i in range(1,rowIndex):
            left = -1
            right = 0
            newRow = []
            while right <= len(row):
                if left == -1 or right == len(row):
                    newRow.append(1)
                    left += 1
                    right += 1
                    continue
                print(left, right, newRow)
                newRow.append(row[left] + row[right])
                left += 1
                right += 1
            row = newRow
        return row


