class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True


        for num in nums:
            for w in range(target, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]
                if dp[target]:
                    return True

        return dp[target]