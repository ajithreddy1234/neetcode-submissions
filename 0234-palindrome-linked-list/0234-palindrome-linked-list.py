# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        check=prev
        x=head
        while check:
            if check.val!=x.val:
                return False
            check=check.next
            x=x.next
        return True

        
        