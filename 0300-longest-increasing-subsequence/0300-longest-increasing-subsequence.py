class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo=[-1 for i in range(n)]
        def solve(i):
            if memo[i]!=-1:
                return memo[i]
            bst=1
            for j in range(i,n):
                if nums[j]>nums[i]:
                    bst=max(bst,1+solve(j))
            memo[i]=bst
            return bst
        fin=0
        for i in range(n):
            fin=max(fin,solve(i))
        return fin
