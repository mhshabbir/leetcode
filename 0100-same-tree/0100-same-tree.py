# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        
         3         3
        / \       / \
        1  n     n   n
        
        """

        if not p and not q:
            return True
        elif p and not q or not p and q:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.left, q.left)

        return p.val == q.val and (left == right == True)