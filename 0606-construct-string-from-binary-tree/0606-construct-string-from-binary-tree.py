# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        1      "1"
        /\
        n n
        if not root:
            return ""
        left = fucntion(root.left)
        right = function(root.right)

        return f"{root.val}" + left + right

        1       "1(2)"
        /\
        2 n
        if not root:
            return ""
        if root.left or (not root.left and root.right):
            left = "(" + fucntion(root.left) ")"
        if root.right:
            right = function(root.right)

        return f"{root.val}" + left + right

        1      1(()3)
        /\
        n 3
        if not root:
            return ""
        if root.left or (not root.left and root.right):
            left = "(" + fucntion(root.left) ")"
        if root.right:
            right = function(root.right)

        return f"{root.val}" + "(" + left + right + ")"
        """
        if not root:
            return ""
        if root.left or (not root.left and root.right):
            left = "(" + self.tree2str(root.left) + ")"
        else:
            left = ""
        if root.right:
            right = "(" + self.tree2str(root.right) + ")"
        else:
            right = ""

        return f"{root.val}" + left + right 