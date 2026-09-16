class Solution:
    def longestCommonSubsequence(self,s1, s2):
        n = len(s1)
        m = len(s2)

        dp=[[-1 for i in range((m+1))] for i in range((n+1))]

        def solve(i, j):

            if i == n or j == m:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            if s1[i] == s2[j]:
                ans = 1 + solve(i + 1, j + 1)

            else:
                ans = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            dp[i][j] = ans
            return ans
        return solve(0,0)