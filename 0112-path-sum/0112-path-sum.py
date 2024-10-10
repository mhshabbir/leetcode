# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
            4                               
           / \
          1   2
         / \    \
        n   2    1
                t = 7
        """ 
        def helper(root, pathSum):
            if not root:
                return False

            pathSum += root.val
            if not root.left and not root.right:
                return pathSum == targetSum
            
            return (helper(root.left, pathSum) or helper(root.right, pathSum))
            
        return helper(root, 0)