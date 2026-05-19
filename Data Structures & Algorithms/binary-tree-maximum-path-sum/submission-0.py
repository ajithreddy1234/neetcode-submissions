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
            if not root:
               return 0
            left=self.g(root.left)
            right=self.g(root.right)
            res=max(res,root.val+left+right)
            df(root.left)
            df(root.right)
        df(root)
        return res




    def g(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=self.g(root.left)
        right=self.g(root.right)
        path=root.val+max(left,right)
        return max(0,path)

        