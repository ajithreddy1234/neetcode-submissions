# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x=[]
        q=deque([root])
        while q:
            node=q.popleft()
            x.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return sorted(x)[k-1]
        