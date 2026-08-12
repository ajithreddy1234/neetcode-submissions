# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        count=0
        dq=deque([root])
        fin=[]
        while dq:
            temp=[]
            count+=1
            for i in range(len(dq)):
                x=dq.popleft()
                temp.append(x.val)
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            if count%2==0:
                fin.append(temp[::-1])
            else:
                fin.append(temp)
        return fin

        