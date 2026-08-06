# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        fa=count-n+1
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        co=1
        while curr:
            if fa==co:
                prev.next=curr.next
            else:
                prev=curr
            co+=1
            curr=curr.next
        return dummy.next
