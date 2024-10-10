# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        curSum = 0
        def helper(root):
            if not root:
                return 0
            if low <= root.val <= high:
                nonlocal curSum
                curSum += root.val
            helper(root.left)
            helper(root.right)
            return curSum
        return helper(root)