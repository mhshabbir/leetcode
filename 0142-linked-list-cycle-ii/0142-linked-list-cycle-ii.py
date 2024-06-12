# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow: break
        
        if not fast or not fast.next:
            return 

        slow2 = head

        while slow:
            if slow == slow2: return slow
            slow = slow.next
            slow2 = slow2.next

       