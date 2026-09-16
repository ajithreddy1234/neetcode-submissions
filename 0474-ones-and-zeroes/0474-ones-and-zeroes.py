class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp=[[0 for i in range(n+1)] for o in range(m+1)]
        for i in range(len(strs)):
            zero=strs[i].count("0")
            one=strs[i].count("1")
            for z in range(m,zero-1,-1):
                for o in range(n,one-1,-1):
                    dp[z][o]=max(dp[z][o],1+dp[z-zero][o-one])
        return dp[m][n]
        