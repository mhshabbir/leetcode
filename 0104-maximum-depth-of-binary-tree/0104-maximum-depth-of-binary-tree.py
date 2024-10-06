# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # level Order:
        # if not root:
        #     return 0
        
        # queue = deque([root])
        # level = 0
        # while queue:
        #     for i in range(len(queue)):
        #         cur = queue.popleft()
        #         if cur.left:
        #             queue.append(cur.left)

        #         if cur.right:
        #             queue.append(cur.right)
        #     level += 1
        # return level
        # preOrder DFS
        if not root:
            return 0
        stack = [(root,1)]
        res = 1

        while stack:
            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))

        return res
