# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U:
        Reverse the list and return the head
        M:
        linked list using 2 pointers
        P:
        use cur and prev pointers 
        place prev's pointer and change its next to behind pointer

                     V
        Temp -> 1 <- 2 -> 3 -> N
                ^
        I
        R
        E:

        """
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

        return prev