# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        First=None
        second=None
        prev=None
        def dfs(node):
            nonlocal First,second,prev
            if not node:
                return
            dfs(node.left)
            if prev and prev.val>node.val:
                if not First:
                    First=prev
                second=node
            prev=node
            dfs(node.right)
        dfs(root)
        First.val,second.val=second.val,First.val

