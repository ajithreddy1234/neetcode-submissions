class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 0
        dp=[[-1 for i in range(len(s)+1)] for i in range(len(s)+1)]
        def solve(start,end):
            if start>=end:
                return 0
            if dp[start][end]!=-1:
                return dp[start][end]
            if s[start]==s[end]:
                ans=solve(start+1,end-1)
            else:
                ans=1+min(solve(start+1,end),solve(start,end-1))
            dp[start][end]=ans
            return ans
        return solve(0,n-1)
        