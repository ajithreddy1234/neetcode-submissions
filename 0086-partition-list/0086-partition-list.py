# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy.next
        prev=dummy
        dom=ListNode(5)
        p=dom
        while curr:
            if curr.val>=x:
                io=curr.next
                p.next=ListNode(curr.val)
                prev.next=io
                curr=io
                p=p.next
            else:
                prev=curr
                curr=curr.next
        ma=dummy
        while ma and ma.next:
            ma=ma.next
        ma.next=dom.next
        return dummy.next



        