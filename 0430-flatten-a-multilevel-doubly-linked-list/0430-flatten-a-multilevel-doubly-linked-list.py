"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head

        while cur:
            if cur.child:
                tmp = cur.next
                cur.next = cur.child
                curChild = cur.child
                curChild.prev = cur
                cur.child = None
                while curChild.next:
                    curChild = curChild.next
                curChild.next = tmp
                if tmp:
                    tmp.prev = curChild

            cur = cur.next
        return head

