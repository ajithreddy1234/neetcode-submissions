# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cu=dummy.next
        previous=dummy
        while cu:
            if cu.val==val:
                previous.next=cu.next
            else:
                previous=cu
            cu=cu.next
        return dummy.next
        