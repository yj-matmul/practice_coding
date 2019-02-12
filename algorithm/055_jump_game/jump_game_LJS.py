def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0 or len(nums) == 1:
        return True
    elif nums[0] == 0:
        return False

    length = len(nums)
    temp = []
    for i in range(length):
        temp.append(i + nums[i])

    curr_index = 0
    jump_range = nums[0]

    while jump_range < length:
        check = max(temp[curr_index:jump_range + 1])  # 점프 범위 내에 점프 범위를 넘어서 갈 수 있는 길이 있나요?
        if check > jump_range:
            curr_index = jump_range + 1
            jump_range = check
        else:
            break
    if jump_range >= length - 1:
        return True
    return False