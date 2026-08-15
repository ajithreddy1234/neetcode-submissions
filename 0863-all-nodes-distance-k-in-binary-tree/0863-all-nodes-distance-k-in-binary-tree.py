# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ma={}
        def dfs(node,parent):
            if not node:
                return
            ma[node]=parent
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        dq=deque([target])
        visited=set()
        visited.add(target)
        level=0
        m=[]
        m.append(target.val)
        while dq:
            if level==k:
                return m
            m=[]
            for i in range(len(dq)):
                x=dq.popleft()
                if x.left and not x.left in visited:
                    dq.append(x.left)
                    visited.add(x.left)
                    m.append(x.left.val)
                if x.right and not x.right in visited:
                    dq.append(x.right)
                    visited.add(x.right)
                    m.append(x.right.val)
                if ma[x] and ma[x] not in visited:
                    dq.append(ma[x])
                    visited.add(ma[x])
                    m.append(ma[x].val)
            level+=1
        return []