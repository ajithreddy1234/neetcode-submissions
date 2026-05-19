# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        lef=self.ma(root.left)
        rig=self.ma(root.right)
        d=lef+rig
        sub=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(d,sub)
    
        


    def ma(self,node):
        if not node :
            return 0
        return 1+max(self.ma(node.right),self.ma(node.left))
        