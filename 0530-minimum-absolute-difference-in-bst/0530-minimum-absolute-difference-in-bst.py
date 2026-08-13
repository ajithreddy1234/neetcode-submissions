# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=float("inf")
        def dfs(node,low,high):
            nonlocal res
            res=min(res,node.val-low,high-node.val)
            if node.left:
                res=min(node.val-node.left.val,res)
                dfs(node.left,low,node.val)
            if node.right:
                res=min(res,node.right.val-node.val)
                dfs(node.right,node.val,high)
        dfs(root,-float("inf"),float("inf"))
        return res
            
        