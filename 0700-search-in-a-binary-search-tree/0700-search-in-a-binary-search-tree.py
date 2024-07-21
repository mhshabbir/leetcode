# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if root == None:
        #     return None

        # queue = [root]
        # while queue:
        #     current = queue.pop(0)
        #     if current.val == val:
        #         return current
        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
            
        # return None
        if not root:
            return None
        
        stack = [root]
        while stack:
            current = stack.pop()
            if current.val == val:
                return current
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            
        return None

