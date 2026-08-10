# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        s=defaultdict(int)
        s[0]=1
        count=0
        def dfs(node,cur_sum):
            nonlocal count
            if not node:
                return 
            cur_sum+=node.val
            count+=s[cur_sum-targetSum]
            s[cur_sum]+=1
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
            s[cur_sum]-=1
        dfs(root,0)
        return count


        