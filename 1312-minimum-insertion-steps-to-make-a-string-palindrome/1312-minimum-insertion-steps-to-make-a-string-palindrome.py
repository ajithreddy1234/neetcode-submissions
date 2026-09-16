class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 0
        dp=[[0 for i in range(len(s)+1)] for i in range(len(s)+1)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                elif s[i]!=s[j]:
                    dp[i][j]=1+min(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1] 
        