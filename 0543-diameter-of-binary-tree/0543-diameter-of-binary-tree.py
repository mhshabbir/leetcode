# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getMax(root):
            if not root:
                return 0
            
            left = getMax(root.left)
            right = getMax(root.right)

            self.maxDiameter = max(self.maxDiameter, left + right)

            return 1 + max(left, right)

        self.maxDiameter = 0
        getMax(root)

        return self.maxDiameter