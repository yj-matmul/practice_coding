def maxCoins(nums):
    values = [1] + nums + [1]
    # temp = [[0 for _ in values] for __ in values]
    temp = [[0 for _ in range(len(values))] for __ in range(len(values)-1)]

    for length in range(1, len(nums) + 1):
        for i in range(0, len(nums) + 1 - length):
            j = i + length + 1
            tp = 0
            for last in range(i + 1, j):
                tp = max(tp, values[i] * values[last] * values[j] + temp[i][last] + temp[last][j])
            temp[i][j] = tp
    return temp[0][-1]


a =maxCoins([2,3,4])
print(a)


# class Solution:
#     def maxCoins(self, nums):
#         l = len(nums)
#         nums = nums + [1]
#         m = [[0 for i in range(l + 1)] for i in range(l + 1)]
#
#         for k in range(0, l):
#             for i in range(l - k):
#                 j = i + k
#                 for x in range(i, j + 1):
#                     m[i][j] = max(m[i][j], m[i][x - 1] + m[x + 1][j] + nums[x] * nums[i - 1] * nums[j + 1])
#         return m[0][l - 1]
