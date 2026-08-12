# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        dq=deque([root])
        final=[]
        while dq:
            cu=0
            m=len(dq)
            for i in range(len(dq)):
                x=dq.popleft()
                cu+=x.val
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            final.append(cu/m)
        return final

        