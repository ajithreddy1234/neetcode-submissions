# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr=root
        def dfs(node):
            nonlocal curr
            if not node:
                return
            left=node.left
            right=node.right
            node.left=None
            if curr!=node:
                curr.right=node
                curr=curr.right
            dfs(left)
            dfs(right)
            return
        dfs(root)
                
        