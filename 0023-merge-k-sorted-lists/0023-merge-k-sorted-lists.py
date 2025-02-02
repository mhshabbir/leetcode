# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import time
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        step 1: add the head of all the list into minheap


        step 2: pop the minheap to remove the min element and add the next eleent of the list back into min heap

        if its None or end of the list dont add it in the list

        """

        dummy = ListNode()
        cur = dummy
        minHeap = []
        for head in lists:
            if head:
                minHeap.append((head.val, time.time(), head.next))

        heapq.heapify(minHeap)

        while minHeap:
            value, seq, nxt = heapq.heappop(minHeap)

            cur.next = ListNode(value)
            cur = cur.next
            if nxt != None:
                heapq.heappush(minHeap, (nxt.val, time.time(), nxt.next))
        
        return dummy.next
        