# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        fin=0
        def dfs(node):
            nonlocal fin
            if not node:
                return
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        return stack[k-1]