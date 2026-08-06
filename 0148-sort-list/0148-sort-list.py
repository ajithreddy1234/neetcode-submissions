# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        heap=[]
        while curr:
            heapq.heappush(heap,curr.val)
            curr=curr.next
        dummy=ListNode(0)
        pr=dummy
        while heap:
            v=heapq.heappop(heap)
            pr.next=ListNode(v)
            pr=pr.next
        return dummy.next
