# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        x=deque([(root,1)])
        left=0
        right=0
        res=1
        while x:
            if len(x)>1:
                left=x[0][1]
                right=x[-1][1]
                res=max(res,right-left+1)
            for i in range(len(x)):
                y,i=x.popleft()
                if y.left:
                    x.append((y.left,2*i))
                if y.right:
                    x.append((y.right,2*i+1))
        return res
            