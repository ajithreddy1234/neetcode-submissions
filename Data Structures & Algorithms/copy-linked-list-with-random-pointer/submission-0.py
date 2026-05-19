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
        x={None : None}

        curr=head
        while curr:
            c=Node(curr.val)
            x[curr]=c
            curr=curr.next

        curr=head
        while curr:
            y=x[curr]
            y.next=x[curr.next]
            y.random=x[curr.random]
            curr=curr.next
        return x[head]

        