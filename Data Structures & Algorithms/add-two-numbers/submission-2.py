# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def rev(head):
            curr=head
            prev=None
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        n1=rev(l1)
        
        n2=rev(l2)
        s1=''
        s2=''
        while n1 :
            s1+=str(n1.val)
            n1=n1.next
        while n2:
            s2+=str(n2.val)
            n2=n2.next
        s=str(int(s1)+int(s2))
        dummy=ListNode(None)
        curr=dummy
        for i in range(len(s)):
            curr.next=ListNode(int(s[len(s)-i-1]))
            curr=curr.next
        return dummy.next
            

