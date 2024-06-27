# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur = head

        while cur and cur.next:
            #saving the previous pointeres
            nextPair = cur.next.next
            second = cur.next

            #swapping the nodes:
            cur.next = nextPair
            second.next = cur
            prev.next = second

            #moving:
            prev = cur
            cur = nextPair
        
        return dummy.next


