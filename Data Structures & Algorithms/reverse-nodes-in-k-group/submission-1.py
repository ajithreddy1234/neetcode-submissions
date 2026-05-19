# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr.val)
            curr=curr.next
        d=[]
        for i in range(k-1,len(nodes),k):
            for m in range(k):
                d.append(nodes[i-m])
        if len(d)<len(nodes):
            for i in range(len(nodes)-len(d)):
                d.extend(nodes[len(d):])

        print(d)
        dummy=ListNode(0)
        cur=dummy
        for l in d:
            cur.next=ListNode(l)
            cur=cur.next
        return dummy.next



        
        
            
            
        
        