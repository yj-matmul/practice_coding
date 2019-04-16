class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        # 길이가 0인 리스트
        if N == 0:
            answer = 0

        else:
            f1 = f2 = 0
            for n in range(N):
                tmp = f2
                f2 = max(f2, f1 + nums[n])
                f1 = tmp
            answer = f2

        return answer
