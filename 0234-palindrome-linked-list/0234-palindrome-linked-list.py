# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        """
        U
        
        M
        P
                  N
        p1             p2                  
        1 -> 2 -> 2 <- 3
                          f 
                  s


        I
        R
        E
        """

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        ptr1 = head
        ptr2 = prev

        while ptr1 != slow:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True  
