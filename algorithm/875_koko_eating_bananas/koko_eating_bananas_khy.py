class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        l = 0
        r = max(piles)

        if len(piles) == H: #무조건 빠지는 경우
            out = r

        else:
            mid = (r - l) // 2 + l

            while l < mid:

                count = 0

                for p in piles: #먹는 시간 계산
                    if p % mid != 0:
                        count += p // mid + 1
                    else:
                        count += p // mid

                if count <= H: #시간이 덜 걸릴 경우
                    r = mid

                else: #시간이 더 걸릴 경우
                    l = mid

                mid = (r - l) // 2 + l #mid값 갱신

            out = r

        return out