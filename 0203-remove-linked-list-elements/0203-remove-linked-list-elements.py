# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # node = ListNode
        # node = head
        # while node:
        #     if node.next.val == val and node.next.next:
        #         node.next = node.next.next
        #     elif node.next.val == val:
        #         node.next = None
        #     node = node.next
        # return head
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next