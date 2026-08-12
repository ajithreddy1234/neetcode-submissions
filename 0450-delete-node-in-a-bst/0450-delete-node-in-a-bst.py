# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            su=root.right
            while su.left:
                su=su.left
            root.val=su.val
            root.right=self.deleteNode(root.right,su.val)
        return root
