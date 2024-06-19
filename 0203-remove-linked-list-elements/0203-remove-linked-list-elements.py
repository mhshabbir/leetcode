# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        U:
        remove the val = 6 from the linkedList
        M
        using a temp node and 2 pointers
        P
        D -> 1 -> 2 -> 3 -> 4 -> 5 -> N
                                 p    c    t
        D -> 1 -> 2 -> 3 -> 4 -> 5 -> N
                            p    c

        I
        R
        E
        """
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next

            else:
                cur = cur.next
                prev = prev.next
        
        return dummy.next
