# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nodes=[]
        while curr:
            nodes.append(curr.val)
            curr=curr.next
        new=nodes[::-1]
        dummy=ListNode(0)
        c=dummy
        counter=0
        while counter<=len(nodes)-1:
            c.next=ListNode(new[counter])
            counter+=1
            c=c.next
        return dummy.next
        
        

        