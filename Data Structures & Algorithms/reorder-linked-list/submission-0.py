class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow.next
        prev=None
        slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        f=head
        s=prev
        while s:
            t1=f.next
            t2=s.next
            f.next=s
            s.next=t1
            f,s=t1,t2

            

        

        


