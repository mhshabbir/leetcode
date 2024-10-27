# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
            1             1
            /\            /\
           2  2           N 2
        """
        def compareTree(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False
            
            return (root1.val == root2.val and compareTree(root1.left, root2.right) and 
            compareTree(root1.right, root2.left))

        return compareTree(root.left, root.right)


            
            
            
            
