# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U: Remove dups that comes after. sorted list
        time and space complexities
        can an empty list be in an input?
        Is it only numbers in the list?

        M:
        Multiple passing

        P:
        while P2:
            check if p2.val == p1.val:
                temp = p2.next
                p1.next = p2.next
                p2 = temp

            else:
                p1 = p1.next
                p2 = p2.next

                p2    T
            1 -> 1 -> 2 -> N
            p1
        I
        R
        E
        """

        if head == None:
            return head

        p1 = head
        p2 = head.next
        while p2:
            print(p2.val)
            if p2.val == p1.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1 = p1.next
                p2 = p2.next
        
        return head