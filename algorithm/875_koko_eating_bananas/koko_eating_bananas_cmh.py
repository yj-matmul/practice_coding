class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        # 변수 설정
        cnt_pile = len(piles)
        mineat_cnt = 1
        maxeat_cnt = math.ceil(max(piles) * cnt_pile / H)


        while mineat_cnt + 1 < maxeat_cnt:
            mid = (mineat_cnt + maxeat_cnt) // 2
            time = sum([math.ceil(pile / mid) for pile in piles])

            # time 이 H 보다 크면 mineat_cnt를 mid 로 변경
            if time > H:
                mineat_cnt = mid
            # 반대경우 maxeat_cnt 를 mid 로 변경
            else:
                maxeat_cnt = mid

        if sum([math.ceil(pile / mineat_cnt) for pile in piles]) <= H:
            answer = mineat_cnt
        else:
            answer = maxeat_cnt

        return answer
