# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        return self._isBalanced(root)

    def _isBalanced(self, root) -> bool:
        if not root:
            return True
        
        heightLeft = self.height(root.left)
        heightRight = self.height(root.right)
        
        if abs(heightLeft - heightRight) > 1:
            return False

        return self._isBalanced(root.left) and self._isBalanced(root.right)
        #                 # 0        -       2
        # return False if abs(heightLeft - heightRight) > 1 else True
        
    def height(self, root):
        if not root:
            return -1
            
        left = 1 + self.height(root.left)
        right = 1 + self.height(root.right)
        
        return max(left, right)