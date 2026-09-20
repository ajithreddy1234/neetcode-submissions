class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        n1 = len(s)
        n2 = len(p)

        dp = [[-1] * (n2 + 1) for _ in range(n1 + 1)]

        def solve(i, j):

            # Both strings exhausted
            if i == n1 and j == n2:
                return True

            # Pattern exhausted, but string remains
            if j == n2:
                return False

            # String exhausted:
            # Remaining pattern must contain only '*'
            if i == n1:
                return all(ch == "*" for ch in p[j:])

            if dp[i][j] != -1:
                return dp[i][j]

            # Exact match or '?'
            if s[i] == p[j] or p[j] == "?":

                ans = solve(i + 1, j + 1)

            # '*' can match zero or more characters
            elif p[j] == "*":

                skip = solve(i, j + 1)

                take = solve(i + 1, j)

                ans = skip or take

            # Ordinary character mismatch
            else:
                ans = False

            dp[i][j] = ans

            return ans

        return solve(0, 0)