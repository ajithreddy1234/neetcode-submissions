# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for head in lists:
            curr=head
            while curr:
                heapq.heappush(heap,curr.val)
                curr=curr.next
        dummy=ListNode(0)
        cu=dummy
        while heap:
            x=heapq.heappop(heap)
            cu.next=ListNode(x)
            cu=cu.next
        return dummy.next

