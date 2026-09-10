# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return 0,0
            c1,s1=dfs(node.left)
            c2,s2=dfs(node.right)
            fc=c1+c2+1
            sc=s1+s2+node.val
            if node.val==sc//fc:
                res+=1
            return fc,sc
        su,count=dfs(root)
        return res
        