# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        seen=set()
        dq=deque([root])
        seen.add(root.val)
        while dq:
            for i in range(len(dq)):
                e=dq.popleft()
                if e.left:
                    if k-e.left.val in seen:
                        return True
                    dq.append(e.left)
                    seen.add(e.left.val)
                if e.right:
                    if k-e.right.val in seen:
                        return True
                    dq.append(e.right)
                    seen.add(e.right.val)
        return False