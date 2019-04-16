def trap(self, height: List[int]) -> int:
    result = 0

    if len(height) < 3:
        return result

    max_right = max(height)
    max_right_i = height.index(max_right)
    for i in range(1, max_right_i + 1):
        max_left = 0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])
        result += min(max_left, max_right) - height[i]

    for i in range(max_right_i, len(height) - 1):
        max_left, max_right = 0, 0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])
        for j in range(i, len(height)):
            max_right = max(max_right, height[j])
        result += min(max_left, max_right) - height[i]

    return result