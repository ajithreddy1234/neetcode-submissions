class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # Move slow by 1
            fast = fast.next.next     # Move fast by 2

            if slow == fast:
                return True

        return False
 

        