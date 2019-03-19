def maxSubArray(self, nums: List[int]) -> int:
    max_point = curr_sum = nums[0]

    for i in nums[1:]:
        curr_sum = max(i, curr_sum + i)
        max_point = max(curr_sum, max_point)

    return max_point