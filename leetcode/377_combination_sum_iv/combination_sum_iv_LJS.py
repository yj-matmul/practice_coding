class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()

        for i in range(nums[0], target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[-1]