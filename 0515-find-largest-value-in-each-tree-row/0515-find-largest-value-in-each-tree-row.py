# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq=deque([root])
        final=[]
        while dq:
            res=-float("inf")
            for i in range(len(dq)):
                x=dq.popleft()
                res=max(res,x.val)
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            final.append(res)
        return final
        