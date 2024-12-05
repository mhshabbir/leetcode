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
        curr = head

        while curr:
            if curr.child:
                temp_next_of_parent = curr.next
                
                # make the child next to curr
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
                
                temp_curr = curr.next
                while temp_curr.next:
                    temp_curr = temp_curr.next
                temp_curr.next = temp_next_of_parent
                temp_next_of_parent.prev = temp_curr

                curr = curr.next

            else:
                curr = curr.next
            
        return head