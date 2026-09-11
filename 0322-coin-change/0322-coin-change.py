class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)

        dp[amount] = 0

        for coin in coins:

            for j in range(amount - coin, -1, -1):

                dp[j] = min(
                    dp[j],
                    1 + dp[j + coin]
                )

        return dp[0] if dp[0] != float("inf") else -1