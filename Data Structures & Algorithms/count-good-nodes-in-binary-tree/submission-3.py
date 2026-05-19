# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def df(root,maxsofar):
            if not root:
                return 0
            isgood = 1 if root.val>=maxsofar else 0
            maxsofar=max(maxsofar,root.val)
            return isgood+df(root.left,maxsofar)+df(root.right,maxsofar)
        return df(root,root.val)
        