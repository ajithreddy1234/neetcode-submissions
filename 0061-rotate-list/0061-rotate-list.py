class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Find length
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        rotations = k % length

        if rotations == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        for _ in range(rotations):
            prev = dummy
            curr = dummy.next

            # Move curr to the last node
            while curr.next:
                prev = curr
                curr = curr.next

            # Remove last node
            prev.next = None

            # Move last node to front
            curr.next = dummy.next
            dummy.next = curr

        return dummy.next