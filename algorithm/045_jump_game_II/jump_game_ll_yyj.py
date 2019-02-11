class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pos: 현 위치에서 가장 멀리 갈 수 있는 범위
        # future: pos의 범위 중에서 가장 멀리 나갈 수 있는 거리
        # cnt: 뛰는 횟수
        pos = future = 0
        cnt = 0

        for n in range(len(nums)):
            # 현재 index가 pos를 넘으면 그간 갱신했던 future만큼 점프
            if n > pos:
                pos = future
                cnt += 1
                # 만약 last index 이상이면 반복문 탈출
                if pos >= len(nums) - 1: break

            # 매 index마다 future 값 갱신
            future = max(future, n + nums[n])

        return cnt
