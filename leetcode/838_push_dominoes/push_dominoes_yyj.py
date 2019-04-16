class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        try:
            N = len(dominoes)
            # str을 list type으로 변환
            domi = []
            for n in range(N):
                domi.append(dominoes[n])

            # R을 거친 다음 얼마나 왔는지 거리를 담을 리스트
            dp = [0] * N
            for n in range(N):
                # .을 만났을 때
                if domi[n] == '.':
                    # 이전에 R을 오래 전에 만난 후
                    if dp[n - 1] > 0:
                        dp[n] = dp[n - 1] + 1
                        domi[n] = 'R'
                    # 이전에 R을 만난 직후
                    elif (domi[n - 1] == 'R') and (n > 0):
                        domi[n] = 'R'
                        dp[n] = 1
                # R이나 L을 만났을 때
                else:
                    # R을 만나면 바로 다음 index로
                    if domi[n] == 'R':
                        continue
                    else:
                        num = dp[n - 1]
                        # L 이전에 R이 있었던 경우
                        if num > 0:
                            # R을 거친 거리가 짝수일 때
                            for i in range(n - num // 2, n):
                                domi[i] = 'L'
                            # R을 거친 거리가 홀수일 때
                            if num % 2:
                                domi[n - num // 2 - 1] = '.'
                        # L 이전에 R이 없는 경우
                        else:
                            while (domi[n - 1] == '.') and (n > 0):
                                domi[n - 1] = 'L'
                                n -= 1

            return ''.join(domi)

        # 도미노 길이가 0이나 1인 경우
        except:
            return dominoes
