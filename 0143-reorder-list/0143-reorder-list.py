# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        curr=second
        prev=None
        while curr:
            ne=curr.next
            curr.next=prev
            prev=curr
            curr=ne
        curr=head
        while prev:
            ne=curr.next
            na=prev.next
            curr.next=prev
            prev.next=ne
            prev=na
            curr=ne
        return head


        