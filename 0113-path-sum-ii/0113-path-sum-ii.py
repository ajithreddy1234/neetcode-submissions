# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(node,cur,total):
            print(cur)
            if not node:
                return
            total+=node.val
            cur.append(node.val)
            if not node.left and not node.right and total==targetSum:
                ans.append(cur[:])
            dfs(node.left,cur,total)
            dfs(node.right,cur,total)
            cur.pop()
        dfs(root,[],0)
        return ans
            
        