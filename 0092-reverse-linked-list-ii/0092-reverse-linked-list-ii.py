# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        curr=prev.next
        for _ in range(right-left):
            print(dummy.next)
            nextt=curr.next
            curr.next=nextt.next
            nextt.next=prev.next
            prev.next=nextt
        return dummy.next


        