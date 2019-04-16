class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 끝에서부터 도착 가능 여부를 따짐
        pos = len(nums) - 1
        for n in range(len(nums) - 2, -1, -1):
            # last index까지 갈 수 있다는 것이 확인되면 도착 위치를 현재 위치로 바꿈
            if n + nums[n] >= pos:
                pos = n

        return pos == 0
