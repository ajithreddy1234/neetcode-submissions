# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cu1=l1
        cu2=l2
        vala=1
        fin1=0
        fin2=0
        while cu1 and cu2:
            fin1+=cu1.val*vala
            fin2+=cu2.val*vala
            cu1=cu1.next
            cu2=cu2.next
            vala*=10
        while cu1:
            fin1+=cu1.val*vala
            cu1=cu1.next
            vala*=10
        while cu2:
            fin2+=cu2.val*vala
            cu2=cu2.next
            vala*=10
        print(fin1+fin2)
        x=str(fin1+fin2)[::-1]
        dummy=ListNode(0)
        c=dummy
        for cu in x:
            c.next=ListNode(int(cu))
            c=c.next
        return dummy.next
        