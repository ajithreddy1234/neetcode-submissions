# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,rem):
            if not node:
                return False
            rem-=node.val
            if not node.left and not node.right and rem==0:
                return rem==0
            return dfs(node.left,rem) or dfs(node.right,rem)
        return dfs(root,targetSum)
            

        