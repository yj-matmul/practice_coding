class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]  # bits array (0은 바로 넣어줌)

        for n in range(1, num + 1):
            bits = 0  # 각 n 마다 bits 초기화

            while n:
                # memoization 활용
                if n < len(ans):
                    bits += ans[n]
                    break
                bits += n % 2  # 나머지 있으면 비트 1이므로
                n //= 2  # 몫을 n을 바꾸고 반복
            ans.append(bits)

        return ans
