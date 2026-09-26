class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], 1 + dp[x - c])

        return dp[amount] if dp[amount] != float('inf') else -1