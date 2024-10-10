# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def dfs(p, q):
            if not p and not q:
                return True
            elif not p and q or p and not q:
                return False
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return p.val == q.val and (left == right == True)

        if dfs(root, subRoot): 
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

