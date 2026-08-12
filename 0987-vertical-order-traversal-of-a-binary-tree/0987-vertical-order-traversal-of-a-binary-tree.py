# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        x = defaultdict(lambda: defaultdict(list))
        dq=deque([(root,0,0)])
        mi,ma=0,0
        while dq:
            for i in range(len(dq)):
                k,l,m=dq.popleft()
                mi=min(mi,l)
                ma=max(ma,l)
                x[l][m].append(k.val)
                if k.left:
                    dq.append((k.left,l-1,m+1))
                if k.right:
                    dq.append((k.right,l+1,m+1))
        print(x)
        final=[]
        for i in range(mi,ma+1):
            m=[]
            for j in x[i]:
                if len(x[i][j])>1:
                    x[i][j].sort()
                for num in x[i][j]:
                    m.append(num)
            final.append(m)
        return final
                    



        