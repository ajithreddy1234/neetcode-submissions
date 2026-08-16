# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return True,float("inf"),float("-inf"),0
            left_bst,left_min,left_max,lef_total=dfs(node.left)
            right_bst,right_min,right_max,rig_total=dfs(node.right)
            if (left_bst and right_bst and left_max<node.val<right_min):
                print(0,node.val)
                res=max(res,lef_total+rig_total+node.val)
                return True,min(left_min,node.val),max(right_max,node.val),lef_total+rig_total+node.val
            return False,float("-inf"),float("inf"),0   
        dfs(root)
        return res 