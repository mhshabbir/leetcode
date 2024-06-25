# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        U:
        Time and space:
        can the list be null?
        Does it always have numbers?
        can there be negatives?
        

        M:
        2 pointers 

        P:
                p1
                 5 -> 2 -> 13 -> 3 -> 8 -> n
                           p2
            move p2 until it finds a val bigger then p1.val, if it reaches Null, move p1 and p2 to p1.next
                
        I:
                   p1
        H ->  13 -> 8 -> n
                        p2       
        R:
        E:
        
        """
        # Stack solution:
        # stack = []

        # cur = head
        # while cur:
        #     while stack and cur.val > stack[-1]:
        #         stack.pop()
        #     stack.append(cur.val)
        #     cur = cur.next

        # dummy = ListNode()
        # cur = dummy

        # for n in stack:
        #     cur.next = ListNode(n)
        #     cur = cur.next
        # return dummy.next
        # "Reverse the linked List and maintain a max"
        """ 
             t
       <- 1  2 -> 3 -> 4 -> 5
  prev    Cur

        """

        def reverse(head):
            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        head = reverse(head)
        cur = head
        curMax = cur.val
        while cur.next:
            if cur.next.val < curMax:
                cur.next = cur.next.next
            else:
                curMax = cur.next.val
                cur = cur.next

        return reverse(head)





            


