class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 0
        last = {}

        for c in s:
            new_dp = (2 * dp + 1 - last.get(c, 0)) % MOD

            last[c] = dp + 1
            dp = new_dp

        return dp