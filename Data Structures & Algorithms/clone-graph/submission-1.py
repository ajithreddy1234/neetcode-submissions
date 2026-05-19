"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        old={}
        old[node]=Node(node.val)
        q=deque([node])
        while q:
            cur=q.popleft()
            for n in cur.neighbors:
                if n not in old:
                    old[n]=Node(n.val)
                    q.append(n)
                old[cur].neighbors.append(old[n])
        return old[node]
        