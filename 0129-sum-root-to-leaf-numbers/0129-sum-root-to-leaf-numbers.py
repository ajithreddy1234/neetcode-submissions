# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        su=0
        stack=[]
        def dfs(node):
            nonlocal su
            if not node:
                return
            stack.append(str(node.val))
            if not node.left and not node.right:
                su+=int("".join(stack))
            dfs(node.left)
            dfs(node.right)
            stack.pop()
            return
        dfs(root)
        return su
        