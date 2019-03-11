class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        answer = 0  # 정답 K

        # piles의 길이가 1일 경우
        if len(piles) < 2:
            if piles[0] >= H:
                answer = piles[0] // H + 1
            else:
                answer = 1
            return answer

        # 최소 K를 찾기 위해 binary search 이용
        low = 0
        high = max(piles)  # low, high가 K의 범위
        while low <= high:
            mid = (low + high) // 2
            time = self.sum_time(piles, mid)
            if time > H:
                low = mid + 1
            elif time < H:
                high = mid - 1
            else:
                # 혹시라도 더 낮은 경우가 있는 경우
                time = self.sum_time(piles, mid - 1)
                if time == H:
                    return mid - 1
                else:
                    return mid

        # binary search 후에도 못 찾을 경우 K값을 하나씩 줄여가며 구함
        for k in range(low, 0, -1):
            time = self.sum_time(piles, k)
            if time <= H:
                return k

    # K가 주어졌을 때 바나나를 다 먹는데까지 걸리는 총 시간을 계산하는 함수
    def sum_time(self, array, k):
        time = 0
        if k == 0: k = 1
        for i in array:
            # 나머지가 있는 경우 몫+1
            if i % k:
                time += i // k + 1
            # 나누어 떨어지는 경우
            else:
                time += i // k

        return time
