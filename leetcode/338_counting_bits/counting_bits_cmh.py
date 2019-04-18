class Solution:
    # 함수 생성
    def counting(self, num):
        # 나머지(0 또는 1) 변수 생성 및 더하기
        cnt = 0
        cnt += num % 2

        # 2로 나눈 몫이 0이 아니면 몫으로 재귀함수 실행하고 나머지(0 또는 1)를 더함
        if num // 2 != 0:
            cnt += self.counting(num // 2)

        # 나머지 return
        return cnt

    def countBits(self, num: int) -> List[int]:
        # 정답 list 변수 생성
        answer = []
        # 클래스 생성
        solve = Solution()

        # 0부터 num 까지 1의 수 찾고 answer 에 append
        for x in range(num + 1):
            answer.append(solve.counting(x))

        return answer
