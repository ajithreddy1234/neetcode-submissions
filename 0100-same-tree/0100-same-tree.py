# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, r1, r2):
        # code here
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if node1.val!=node2.val:
                return False
            return (dfs(node1.left,node2.left) and dfs(node1.right,node2.right))
        return dfs(r1,r2)