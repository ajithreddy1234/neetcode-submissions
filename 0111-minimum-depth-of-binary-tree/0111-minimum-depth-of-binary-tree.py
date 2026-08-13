# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        elif not node.left:
            return 1+self.minDepth(node.right)
        elif not node.right:
            return 1+self.minDepth(node.left)
        else:
            return 1+min(self.minDepth(node.left),self.minDepth(node.right))

        