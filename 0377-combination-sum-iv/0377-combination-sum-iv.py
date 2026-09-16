class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        # Sums outside → permutations
        for current_sum in range(1, target + 1):
            for num in nums:
                if num <= current_sum:
                    dp[current_sum] += dp[current_sum - num]

        return dp[target]
        