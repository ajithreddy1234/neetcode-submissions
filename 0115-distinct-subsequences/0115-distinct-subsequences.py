class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        memo = {}

        def solve(i, j):

            # Target completely matched
            if j == m:
                return 1

            # Source exhausted, target incomplete
            if i == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:

                take = solve(i + 1, j + 1)

                skip = solve(i + 1, j)

                ans = take + skip

            else:

                ans = solve(i + 1, j)

            memo[(i, j)] = ans

            return ans

        return solve(0, 0)