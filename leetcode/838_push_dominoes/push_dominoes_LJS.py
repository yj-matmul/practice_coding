def pushDominoes(dominoes):
    """
    :type dominoes: str
    :rtype: str
    """
    dp1 = []
    for i in range(len(dominoes)):
        dp1.append(dominoes[i])
    # dp = [tmp[:]] * len(dominoes)
    dp2 = []

    if dominoes == '.': return '.'

    if '.' not in dp1:
        return dominoes

    while True:
        for j in range(len(dominoes)):
            dp2.append(dp1[j])

            # . 아닌경우 패스
            if dp2[j] != '.':
                continue

            # 가장 왼쪽
            if j == 0:
                if dp1[j + 1] == 'L':
                    dp2[j] = 'L'
                continue

            # 가장 오른쪽
            if j == len(dominoes) - 1:
                if dp1[j - 1] == 'R':
                    dp2[j] = 'R'
                continue

            # 가운데
            if (dp1[j - 1] == 'R') and (dp1[j + 1] != 'L'):
                dp2[j] = 'R'
            elif (dp1[j - 1] == 'R') and (dp1[j + 1] == 'L'):
                pass
            elif (dp1[j - 1] != 'R') and (dp1[j + 1] == 'L'):
                dp2[j] = 'L'

        if dp1 == dp2:
            break

        if '.' not in dp2:
            break
        dp1 = dp2
        dp2 = []

    return ''.join(dp2)

    #
    # if '.' not in dp1:
    #     return dominoes
    #
    # for i in range(1, len(dominoes)):
    #     if '.' not in dp[i - 1]:
    #         return dp[i - 1]
    #
    #     for j in range(len(dominoes)):
    #
    #         # . 아닌경우 패스
    #         if dp[i][j] != '.':
    #             print('0',i,j)
    #             continue
    #         # 가장 왼쪽
    #         if j == 0 :
    #             if dp[i-1][j+1] == 'L':
    #                 print('1',i,j)
    #                 dp[i][j] = 'L'
    #             continue
    #
    #         # 가장 오른쪽
    #         if j == len(dominoes):
    #             if dp[i-1][j-1] == 'R':
    #                 print('2',i,j)
    #                 dp[i][j] ='R'
    #             continue
    #
    #         # 가운데
    #         if (dp[i-1][j-1] == 'R') and (dp[i-1][j+1] != 'L'):
    #             print('3',i,j)
    #             dp[i][j] = 'R'
    #         elif (dp[i-1][j-1] == 'R') and (dp[i-1][j+1] == 'L'):
    #             print('4',i,j)
    #         elif (dp[i-1][j-1] != 'R') and (dp[i-1][j+1] == 'L'):
    #             print('5',i,j)
    #             dp[i][j] = 'L'
    #         else:
    #             print('6',i,j)
    #
    #     print(dp[i])
    #
    #     if dp[i] == dp[i-1]:
    #         return dp[i]


a = pushDominoes(".L.R...LR..L..")
a