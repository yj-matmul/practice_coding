def minEatingSpeed(self, piles: List[int], H: int) -> int:
    # hi = 한시간에 먹어야 되는 최대 양
    # lo = 한시간에 먹어야 되는 최소 양 - 1
    high = math.ceil(sum(piles) / (H - len(piles) + 1))
    low = math.floor(sum(piles) / H)

    while high - low > 1:
        mid = (high + low) // 2

        # 중간값 = 한번에 먹을 수 있는 바나나 양
        # pile 을 중간값으로 나눈다 = 몇번에 pile을 먹을 수 있는가
        # 올림 인 이유는 0.xxx 여도 1번의 횟수를 소모하기 때문
        # h는 총 필요한 시간
        h = sum(map(lambda x: math.ceil(x / mid), piles))

        if h > H:
            low = mid
        else:
            high = mid

    return high