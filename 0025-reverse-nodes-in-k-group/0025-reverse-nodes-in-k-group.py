# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        c=head
        length=0
        while c:
            length+=1
            c=c.next
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        ch=dummy.next
        count=1
        for _ in range(length//k):
            while ch and ch.next and count<k:
                hi=ch.next
                ch.next=hi.next
                hi.next=prev.next
                prev.next=hi
                count+=1
            prev=ch
            ch=ch.next
            count=1
        return dummy.next
            



        
        