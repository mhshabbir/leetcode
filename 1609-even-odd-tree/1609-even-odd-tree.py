# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
        
        queue = deque([root])
        even = True
        while queue:
            level = [float('-inf') if even else float('inf')]

            for _ in range(len(queue)):
                cur = queue.popleft()
                if even and cur.val > level[-1] and cur.val % 2 == 1:
                    level.append(cur.val)
                elif not even and cur.val < level[-1] and cur.val % 2 == 0:
                    level.append(cur.val)
                else:
                    return False

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            even = not even

        return True
            