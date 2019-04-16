def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # buy = min(buy, prices[i])시 첫번째 prices[i]를 buy로 받기 위함
    buy = 10 ** 100

    # answer의 값을 0으로 설정
    answer = 0

    # prices의 끝까지 실행
    for i in range(len(prices) - 1):
        # sell을 prices[i+1]로 지정
        sell = prices[i + 1]
        # buy의 비교
        buy = min(buy, prices[i])
        # profit이 더 클경우 answer 값 변경
        if sell - buy > answer:
            answer = sell - buy

    return answer
