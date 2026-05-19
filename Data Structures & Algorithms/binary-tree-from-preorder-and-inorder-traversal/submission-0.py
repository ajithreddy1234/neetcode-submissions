# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pr=0
        ir=0
        def df(limit):
            
            nonlocal pr
            nonlocal ir
            if pr>=len(preorder):
                return None
            if inorder[ir]==limit:
                ir+=1
                return None
            root=TreeNode(preorder[pr])
            pr+=1
            root.left=df(root.val)
            root.right=df(limit)
            return root
        return df(float("inf"))
        