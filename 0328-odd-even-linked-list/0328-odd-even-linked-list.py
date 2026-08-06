# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n=0
        curr=head
        prev=None
        dummy=ListNode(0)
        po=dummy
        while curr:
            if n==1 or n%2!=0:
                d=curr.next
                prev.next=d
                po.next=ListNode(curr.val)
                po=po.next
                curr=d 
            else:
                prev=curr
                curr=curr.next
            n+=1
        c=head
        print(c)
        while c and c.next:
            c=c.next
        c.next=dummy.next
        print(head)
        return head
        
        
        

