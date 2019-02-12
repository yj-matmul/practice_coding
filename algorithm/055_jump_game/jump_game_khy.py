class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if 0 not in nums: #0이 없을 경우 무조건 성공
            result = True

        else:
            dp = 0 #dp(이동 수)
            count = 1 #남은 이동 수
            idx = 0 #어디까지 갔는지
            for i in range(len(nums)):
                count -= 1 #한번 움직였으니까 남은 이동 수 빼주기
                idx = i
                if nums[i] >= count: #점프 수를 바꾸는 경우
                    dp = nums[i]
                    count = nums[i]

                else: #안바꾸는 경우
                    dp = count

                if dp == 0: #점프 수가 다 된 경우
                    print('stop')
                    break

            # T/F판별
            if dp > 0 or (idx + 1) == len(nums):
                result = True
            else:
                result = False

        return result