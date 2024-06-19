# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U: 
        Sorted List
        Is there any empty node
        what happens if there is only 1 element


        M:
        Two Pointers

        P:
         P    C   T
         N <-  1  2 <- 3 <- 4 <- 5 -> N
          p -> N
        """

        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev