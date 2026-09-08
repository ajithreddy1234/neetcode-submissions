class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0]=0
        for i in range(m):
            for j in range(n):
                if 0<=i-1<m:
                    if i-1==0 and j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]+=dp[i-1][j]
                if 0<=j-1<n:
                    if j-1==0 and i==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]+=dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]

        