# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        x=set()
        while fast:
            if fast in x:
                return fast
            x.add(fast)
            fast=fast.next

        return None
