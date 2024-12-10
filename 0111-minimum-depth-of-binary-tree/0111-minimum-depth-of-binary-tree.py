# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.count = float('inf')
        if not root:
            return 0

        def findMin(node, depth):
            if not node:
                return 0
            
            if node.left == node.right == None:
                self.count = min(self.count, depth + 1)
                return
            findMin(node.left, depth + 1)
            findMin(node.right, depth + 1)

        findMin(root, 0)
        return self.count