# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        U:
        Return the node where both list meet
        Can a list be empty?
        Does the 2 list always meet at the start of the third list
        do i have to produce the steps missed?

        M:
        iterate through one list only inorder to check its evaluation
        P:

        4 -> 1 -> 
                    8 -> 4 -> 5
    5 -> 6 -> 1 -> 



        I
        R
        E
        """

        p1 = headA
        p2 = headB
        dupSet = set()
        while p1:
            dupSet.add(p1)
            p1 = p1.next
        
        while p2:
            if p2 in dupSet:
                return p2
            else:
                p2 = p2.next

        return None 
