# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=0
        curr=root
        while curr:
            left+=1
            curr=curr.left
        right=0
        curr=root
        while curr:
            right+=1
            curr=curr.right
        if left==right:
            return 2**left-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

        