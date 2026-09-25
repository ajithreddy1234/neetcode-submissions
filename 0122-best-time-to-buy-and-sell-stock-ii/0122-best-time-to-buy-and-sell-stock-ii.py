class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*2 for i in range(n)]
        def solve(i,j):
            if i==n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if j==0:
                but=-nums[i]+solve(i+1,1)
                skip=solve(i+1,0)
                dp[i][j]=max(but,skip)
            else:
                sel=nums[i]+solve(i+1,0)
                cont=solve(i+1,1)
                dp[i][j]=max(sel,cont)
            return dp[i][j]
        return solve(0,0)


            

            





            

            


        