# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i,n in enumerate(lists):
            if n:
                heapq.heappush(h,(n.val,i,n))
        d=ListNode(9)
        curr=d
        while h:
            l,i,m=heapq.heappop(h)
            curr.next=m
            curr=curr.next
            if m.next:
                heapq.heappush(h,(m.next.val,i,m.next))
            
        return d.next
            
        


        