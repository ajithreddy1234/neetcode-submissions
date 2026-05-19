# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        
        counter=0
        if n == length:
            return head.next
        curr1=head
        while curr1:
            counter+=1                  
            if (length-counter)==n:
                
                curr1.next=curr1.next.next
            curr1=curr1.next
        return head
        

            

        

        