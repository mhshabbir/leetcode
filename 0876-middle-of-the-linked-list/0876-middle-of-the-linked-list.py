# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U: Remove the middle node of the list.
        is the list sorted?
        Time and space you are looking for?
        what happens at empty list?
        Does the val matter in this case?


        M:
        slow and fast pointer


        P:
        have a fast pointer and a slow pointer, when the fast pointer reaches the end the slow pointer is in the middle

        I:
        while fast and fast.next

                            f
        1 -> 2 -> 3 -> 4 -> 5
                  s
                                    f
        1 -> 2 -> 3 -> 4 -> 5 -> 6
                       s
        R:

        E:
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
