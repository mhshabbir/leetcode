# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        def getLenAndTail(head):
            counter = 1
            cur = head
            while cur.next:
                cur = cur.next
                counter += 1
            return counter, cur
        
        
        listLen, tail = getLenAndTail(head)
        k = k % listLen
        cur = head
        for i in range(listLen - k -1):
            cur = cur.next
        
        tail.next = head
        head = cur.next
        cur.next = None

        return head
        
