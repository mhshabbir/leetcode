# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.minPath = float('inf')
        def dfs(root, curDepth):
            if not root:
                return 0

            if not root.left and not root.right:
                self.minPath = min(self.minPath, curDepth + 1)
            
            dfs(root.left, curDepth + 1)
            dfs(root.right, curDepth + 1)
            
        dfs(root, 0)
        return self.minPath