# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node1,node2):
            if not node2 and not node1:
                return True
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            return check(node1.left,node2.left) and check(node1.right,node2.right)
        x=deque([root])
        while x:
            y=x.pop()
            if y.val==subRoot.val:
                if check(y,subRoot):
                    return True
            if y.left:
                x.append(y.left)
            if y.right:
                x.append(y.right)
        return False