class Solution:
    def longestCommonSubsequence(self,s1, s2):
        n = len(s1)
        m = len(s2)

        memo = {}

        def solve(i, j):

            if i == n or j == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                ans = 1 + solve(i + 1, j + 1)

            else:
                ans = max(
                    solve(i + 1, j),
                    solve(i, j + 1)
                )

            memo[(i, j)] = ans
            return ans

        return solve(0, 0)