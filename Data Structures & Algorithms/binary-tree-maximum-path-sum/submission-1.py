# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-float("inf")
        def df(root):
            nonlocal res
            if not root :
                return 0
            left=df(root.left)
            right=df(root.right)
            left=max(0,left)
            right=max(0,right)
            res=max(res,root.val+left+right)
            return root.val+max(left,right)
        df(root)
        return res
        