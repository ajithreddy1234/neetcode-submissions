# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        curr=head
        sta=[]
        while curr:
            sta.append(curr.val)
            curr=curr.next
        min_va=float("inf")
        for i in range(1,len(sta)-1):
            if sta[i-1]<sta[i]>sta[i+1] or sta[i-1]>sta[i]<sta[i+1]:
                if critical:
                    min_va=min(min_va,i-critical[-1])
                critical.append(i)
        print(critical)
        if len(critical)<=1:
            return [-1,-1]
        else:
            return [min_va,critical[-1]-critical[0]]

