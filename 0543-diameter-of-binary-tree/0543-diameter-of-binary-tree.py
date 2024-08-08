# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        keep a max left and max right and return to your parent + 1
        
        """
        res = 0

        def maxdsf(root):
            if not root:
                return 0
            
            left = maxdsf(root.left)
            right = maxdsf(root.right)

            nonlocal res
            res = max(res, left + right)

            return 1 + max(left, right)

        maxdsf(root)
        return res
            