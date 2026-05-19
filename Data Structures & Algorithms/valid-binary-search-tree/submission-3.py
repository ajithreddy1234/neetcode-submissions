# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append((root,-float("inf"),float("inf")))
        while q:
            node,lef,rig=q.popleft()
            if not (lef<node.val<rig):
                return False
            if node.left:
                q.append((node.left,lef,node.val))
            if node.right:
                q.append((node.right,node.val,rig))

        return True



            

        