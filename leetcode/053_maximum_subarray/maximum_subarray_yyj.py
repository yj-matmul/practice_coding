class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)

        for i in range(len(nums) - 1):
            # 앞에서부터 i+1번째 수가 포함된 subarray 중 가장 큰 값을 dp에 저장
            dp[i + 1] = max(dp[i] + nums[i + 1], nums[i + 1])
        return max(dp)
