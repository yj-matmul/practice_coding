def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # temp = [0]
    # for i in range(len(prices)-1, 0, -1):
    #     for j in range(i - 1, -1, -1):
    #         temp[0] = max(temp[0], prices[i] - prices[j])
    #         print(temp[0])
    #
    # return temp[0]

    try:
        buy = prices[0]
        sell = prices[1]
        temp = [sell - buy, 0]
        for i in range(len(prices)):
            if i > 0:
                if prices[i - 1] < buy:
                    buy = prices[i - 1]
                sell = prices[i]
            temp[1] = sell - buy
            if temp[1] > temp[0]:
                temp[0] = temp[1]

        if temp[0] < 0:
            return 0
    except:
        return 0

    return temp[0]

    # if len(prices) <= 1:
    #     return 0
    # else:
    #     buy = prices[0]
    #     sell = prices[1]
    #     temp = [sell - buy, 0]
    #     for i in range(len(prices)):
    #         if i > 0:
    #             if prices[i - 1] < buy:
    #                 buy = prices[i - 1]
    #             sell = prices[i]
    #         temp[1] = sell - buy
    #         if temp[1] > temp[0]:
    #             temp[0] = temp[1]
    #
    #     if temp[0] < 0:
    #         return 0
    #
    # return temp[0]



print(maxProfit([7,6,4,3,9]))