# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        key_map = defaultdict(list)
        print(queue)
        min_key = float('inf')
        max_key = float('-inf')

        while queue:
            for _ in range(len(queue)):
                cur, key = queue.popleft()
                # print(node)
                # print(queue)
                # cur, key = node[0], node[1]

                key_map[key].append(cur.val)
                min_key = min(min_key, key)
                max_key = max(max_key, key)

                if cur.left:
                    queue.append((cur.left, key - 1))
                
                if cur.right:
                    queue.append((cur.right, key + 1))
        
        result = []

        for key in range(min_key, max_key + 1):
            result.append(key_map[key])
        
        return result

