def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    buy = 0
    sell = 0
    cash = 0

    for i in range(1, len(prices)):
        buy = min(prices[:i])
        sell = max(prices[i:])

        if buy < sell:
            if cash < sell - buy:
                cash = sell - buy

        if prices[i:] == sorted(prices[i:], reverse=True):
            break

    return cash


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
