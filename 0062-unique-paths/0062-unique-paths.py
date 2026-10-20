class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)] for i in range(m)]
        def solve(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            x=0
            if i+1<m:
                x+=solve(i+1,j)
            if j+1<n:
                x+=solve(i,j+1)
            dp[i][j]=x
            return x
        return solve(0,0)
        