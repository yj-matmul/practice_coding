def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    answer = []
    for n in range(len(nums)):
        for m in range(n + 1, len(nums)):
            if nums[n] + nums[m] == target:
                answer.append(n)
                answer.append(m)
                break
        break

    return answer
