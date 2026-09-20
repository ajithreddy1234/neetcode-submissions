class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[n1][n2]=True
        for i in range(n2-1,-1,-1):
            if p[i]=="*":
                dp[n1][i]=dp[n1][i+1]
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if s[i]==p[j] or p[j]=="?":
                    dp[i][j]=dp[i+1][j+1]
                elif p[j]=="*":
                    dp[i][j]=dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i][j]=False
        return dp[0][0]