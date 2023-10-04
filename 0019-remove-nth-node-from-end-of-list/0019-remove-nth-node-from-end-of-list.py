# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow = head
        # fast = head.next
        #                     #head = [1,2,3,4,5], n = 2 i=0
        #                     #        s^f^
        #                     #head = [1,2,3,4,5,N], n = 2 i=1
        #                     #          s^  f^
        #                     #head = [1,2,3,4,5,N], n = 2  i=2
        #                     #           s^    f^
        # slowcounter = 0
        
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     slowcounter += 1

        # totalLen = 0
        # if fast == None:
        #     totalLen = slowcounter * 2 +1
        # else:
        #     totalLen = slowcounter * 2
        
        # target = totalLen - n

        # while slowcounter <= target:
        #     if slowcounter + 1 == target:
        #         slow.next = slow.next.next
        #     else:
        #         slow = slow.next

        # return head

        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        while n != 0:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next

            