# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def df(root,depth):
            if not root:
                return None
            if len(res)==depth:
                res.append([])
            res[depth].append(root.val)
            df(root.left,depth+1)
            df(root.right,depth+1)

        df(root,0)
        return res
        
        