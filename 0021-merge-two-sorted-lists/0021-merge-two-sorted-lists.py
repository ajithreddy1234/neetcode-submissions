# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        final=dummy
        cur1=list1
        cur2=list2
        while cur1 and cur2:
            if cur1.val>=cur2.val:
                new_node=ListNode(cur2.val)
                final.next=new_node
                final=final.next
                cur2=cur2.next
            else:
                new_node=ListNode(cur1.val)
                final.next=new_node
                final=final.next
                cur1=cur1.next
        if cur1:
            while cur1:
                new_node=ListNode(cur1.val)
                final.next=new_node
                final=final.next
                cur1=cur1.next
        elif cur2:
            while cur2:
                new_node=ListNode(cur2.val)
                final.next=new_node
                final=final.next
                cur2=cur2.next
        return dummy.next




        