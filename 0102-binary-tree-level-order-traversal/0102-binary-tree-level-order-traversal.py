# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq=deque([root])
        final=[]
        while dq:
            temp=[]
            for i in range(len(dq)):
                x=dq.popleft()
                temp.append(x.val)
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            final.append(temp)
        return final            
        