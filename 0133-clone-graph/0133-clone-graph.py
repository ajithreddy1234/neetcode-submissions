"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copies={}
        def dfs(some):
            if some in copies:
                return copies[some]
            mg=Node(some.val)
            copies[some]=mg
            for nei in some.neighbors:
                mg.neighbors.append(dfs(nei))
            return mg
        return dfs(node)