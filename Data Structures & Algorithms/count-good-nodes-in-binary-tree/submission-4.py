# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=deque()
        q.append((root,-float("inf")))
        res=0
        while q:
            node,m=q.popleft()
            if node.val>=m:
                res+=1
            if node.left:
                q.append((node.left,max(node.val,m)))
            if node.right:
                q.append((node.right,max(node.val,m)))
        return res

