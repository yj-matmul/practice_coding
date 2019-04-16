class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in nums[1:]:
            dp.append(max(dp[-1] + i, i))

        return max(dp)