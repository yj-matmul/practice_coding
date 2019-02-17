class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        # days: 정답 리스트 / stack: 뒤에서부터 큰 값의 index를 저장할 메모리
        days = [0] * len(T)
        stack = [len(T) - 1]

        for n in range(len(T) - 2, -1, -1):
            # stack 마지막 index의 값보다 크면 다음 큰 값과 비교
            while (len(stack)) and (T[n] >= T[stack[-1]]):
                stack.pop()
            # stack에 아무것도 없을 경우 이 값이 가장 큰 경우
            if len(stack):
                days[n] = stack[-1] - n
            # 매 순간 stack에 index 저장
            stack.append(n)

        return days
