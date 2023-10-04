# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     hashList = {}
    #     while head:
    #         if head in hashList and hashList[head] > 1:
    #             return True
    #         else:
    #             hashList[head] = 1 + hashList.get(head,0)
    #         head = head.next
        
    #     return False

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
