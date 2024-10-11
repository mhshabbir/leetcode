# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
            2            4
            /\          / \
           1  5        1   5
            [1,5] == [1, 5]

            2
           / \
          n   n 

        """
        def helper(root, arr):
            if not root:
                return 
            if not root.left and not root.right:
                arr.append(root.val)
                return arr
            helper(root.left, arr)
            helper(root.right, arr)

            return arr

        return helper(root1, []) == helper(root2, [])
            

