class Solution:
    def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        temp = [0 for i in range(len(nums))]
        temp[0] = nums[0]
        temp[1] = max(nums[0], nums[1])
        result = temp[1]

        for i in range(2, len(nums)):
            temp[i] = max(temp[i-2] + nums[i], temp[i-1])
            if temp[i] > result:
                result = temp[i]

        return result

