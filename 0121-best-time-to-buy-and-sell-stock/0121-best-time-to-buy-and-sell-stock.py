class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        memo=[[-1  for i in range(2)] for i in range(len(nums)+1)]
        def solve(i,can):
            if i==len(nums):
                return 0
            print(i,can)
            if memo[i][can]!=-1:
                return memo[i][can]
            if can==1:
                m=-nums[i]+solve(i+1,0)
                n=solve(i+1,1)
                memo[i][can]=max(m,n)
                return memo[i][can]
            else:
                n=nums[i]
                m=solve(i+1,0)
                memo[i][can]=max(n,m)
                return memo[i][can]
        return solve(0,1)