# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
            3
           / \
           n  n
    
             1 
            / \
           4 2
          / \
        1 3   4 1
          /\  /\

        """
        # if not root:
        #     return 0
        
        # left = self.isBalanced(root.left)
        # right = self.isBalanced(root.right)

        
        # if abs(left - right) > 1:
        #     return False
        # else:
        #     return 
        self.balanceNode = True
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                self.balanceNode = False
            return 1 + max(left,right)
        dfs(root)
        return self.balanceNode


