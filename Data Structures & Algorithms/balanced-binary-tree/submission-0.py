# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack=[root]
        mp={None:0}

        while stack:
            n=stack[-1]
            if n.left and n.left not in mp:
                stack.append(n.left)
            elif n.right and n.right not in mp:
                stack.append(n.right)
            else:
                m=stack.pop()
                l=mp[m.left]
                r=mp[m.right]
                if l-r>1 or l-r<-1:
                    return False
                mp[m]=1+max(l,r)
        return True

    
        