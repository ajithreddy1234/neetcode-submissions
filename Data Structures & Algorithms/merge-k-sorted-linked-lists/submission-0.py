# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node=[]
        for k in lists:
            while k:
                node.append(k.val)
                k=k.next
        node.sort()
        res=ListNode(0)
        cur=res
        for n in node:
            cur.next=ListNode(n)
            cur=cur.next
        return res.next
        