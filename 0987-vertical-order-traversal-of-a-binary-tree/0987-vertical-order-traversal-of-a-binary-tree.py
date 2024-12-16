# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0, 0)])

        key_map = defaultdict(list)
        min_key = float('inf')
        max_key = float('-inf')

        while queue:
            for _ in range(len(queue)):
                cur, y, x = queue.popleft()

                key_map[x].append((cur.val, y))
                min_key = min(min_key, x)
                max_key = max(max_key, x)

                if cur.left:
                    queue.append((cur.left, y + 1, x - 1))

                if cur.right:
                    queue.append((cur.right, y + 1, x + 1))


        result = []

        for key in range(min_key, max_key + 1):
            item = key_map[key]

            item.sort(key = lambda x: (x[1], x[0]))
            result_item_array = []
            for node in item:
                result_item_array.append(node[0])
            
            result.append(result_item_array)
        
        return result
