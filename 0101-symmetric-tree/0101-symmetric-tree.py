# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            return False
        if not root.right:
            return False
        if root.left.val!=root.right.val:
            return False
        dq=deque([root.left,root.right])
        while dq:
            if len(dq)%2!=0:
                return False
            left=[]
            right=[]
            j=len(dq)//2
            for i in range(j):
                x=dq.popleft()
                if x.left:
                    left.append(x.left.val)
                    dq.append(x.left)
                else:
                    left.append(None)
                if x.right:
                    left.append(x.right.val)
                    dq.append(x.right)
                else:
                    left.append(None)
            for i in range(j):
                node=dq.popleft()
                if node.left:
                    right.append(node.left.val)
                    dq.append(node.left)
                else:
                    right.append(None)
                if node.right:
                    right.append(node.right.val)
                    dq.append(node.right)
                else:
                    right.append(None)
            if left!=right[::-1]:
                return False
        return True

            
                    
        

        