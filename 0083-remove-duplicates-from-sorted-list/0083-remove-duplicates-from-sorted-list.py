# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iterate in the list and 
        head = [1,1,2]
                ^ ^ 
        """
        if head == None or head.next == None:
            return head

        ptr1 = head
        ptr2 = head.next

        while ptr1 and ptr2:
            if ptr1.val == ptr2.val:
                # temp = ptr2
                ptr1.next = ptr2.next
                ptr2 = ptr1.next
            else:
                ptr1 = ptr2
                ptr2 = ptr2.next
        return head