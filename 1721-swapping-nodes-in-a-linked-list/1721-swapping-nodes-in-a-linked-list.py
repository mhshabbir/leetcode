# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        U
        Remove nodes at kth from begining and the end
        can we manupulate the list
        
        M
        count the nodes using fast and slow pointers
        fast and slow pointers

        P:
        the total nodes in the list using fast pointers
        use 2 pointers to swap the values

        I
        R
        E
        """
        fast = head
        count = 1

        while fast and fast.next:
            fast = fast.next.next
            count += 2
        if fast == None:
            count -= 1
        ptr1 = head
        for i in range(1, k):
            ptr1 = ptr1.next
       
        ptr2 = head
       
        for i in range(1,(count-k+1)):
            ptr2 = ptr2.next
        
        ptr1.val, ptr2.val = ptr2.val, ptr1.val

        return head