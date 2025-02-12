# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
            or
           / \
          T   F -> T
        """
        if not root.left and not root.right:
            return root.val
        left = self.evaluateTree(root.left) #True
        right = self.evaluateTree(root.right) #False

        # if root.val == 2:
        #     return left or right
        # else:
        #     return left and right

        return (left or right) if root.val == 2 else (left and right)
