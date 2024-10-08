# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """

                7  3
                /    \    
                4 2    9  1
            / \
        1  3     5  1
            / \
        n   n 

             4 2  
            / \
        1  3     5  1
          / \   
         n   n 
        """
        self.maxDiameter = 0
        
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.maxDiameter = max(self.maxDiameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.maxDiameter