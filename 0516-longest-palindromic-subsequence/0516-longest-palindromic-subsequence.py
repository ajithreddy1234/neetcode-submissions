class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[-1 for i in range(len(s)+1)] for _ in range(len(s)+1)]
        def solve(start,end):
            if start==end:
                return 1
            if start>end:
                return 0
            if dp[start][end]!=-1:
                return dp[start][end]
            if s[start]==s[end]:
                ans=2+solve(start+1,end-1)
            else:
                ans=max(solve(start+1,end),solve(start,end-1))
            dp[start][end]=ans
            return ans
        return solve(0,n-1)
