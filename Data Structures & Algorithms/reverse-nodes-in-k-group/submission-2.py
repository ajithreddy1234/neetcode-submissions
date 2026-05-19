# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        gp=dummy
        while True:
            kth=self.kk(gp,k)
            if not kth:
                break
            gn=kth.next
            prev=kth.next
            curr=gp.next
            while curr!=gn:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=gp.next
            gp.next=kth
            gp=temp
        return dummy.next
    def kk(self,gp,k):
        curr=gp
        while k and curr:
            curr=curr.next
            k-=1
        return curr





        
        
            
            
        
        