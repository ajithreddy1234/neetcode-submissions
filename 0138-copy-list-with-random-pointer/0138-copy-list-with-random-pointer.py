"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        x={None:None}
        while curr:
            x[curr]=Node(curr.val)
            curr=curr.next
        cu=head
        while cu:
            d=x[cu]
            d.next=x[cu.next]
            d.random=x[cu.random]
            cu=cu.next
        return x[head]

