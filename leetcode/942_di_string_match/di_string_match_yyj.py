class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)

        # output의 첫 시작 설정
        if S[0] == 'I':
            answer = [0]
            cntI, cntD = 1, 0
        else:
            answer = [N]
            cntI, cntD = 0, 1

        # 문자열에 따라 리스트에 적당한 요소를 집어넣음
        for n in range(1, N):
            if S[n] == 'I':
                answer.append(cntI)
                cntI += 1
            else:
                answer.append(N - cntD)
                cntD += 1

        # 마지막 숫자 채우기
        answer.append(cntI)

        return answer