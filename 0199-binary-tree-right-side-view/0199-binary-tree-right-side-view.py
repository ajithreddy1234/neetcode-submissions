# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        final=[]
        dq=deque([root])
        while dq:
            ss=len(dq)
            for i in range(ss):
                x=dq.popleft()
                if i==ss-1:
                    final.append(x.val)
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
        return final