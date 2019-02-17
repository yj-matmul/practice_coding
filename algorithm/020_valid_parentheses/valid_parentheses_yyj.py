class Solution:
    def isValid(self, s: 'str') -> 'bool':
        # 열림 기호, 닫힘 기호 리스트
        open_chars = ['(', '{', '[']
        close_chars = [')', '}', ']']

        # answer: 정답 / stack: 열림 기호를 담을 메모리
        answer = True
        stack = []
        for char in s:
            # 열림 기호면 stack에 저장
            if char in open_chars:
                stack.append(open_chars.index(char))
            # 닫힘 기호이고 stack에 아무것도 없으면 False
            elif len(stack) == 0:
                answer = False
                break
            else:
                # 닫힘 기호면 stack 끝에 담긴 최종 기호와 비교
                idx = close_chars.index(char)
                if idx != stack.pop(): answer = False

        # 위 과정을 거친 뒤에도 stack에 뭔가 남을 경우 False
        if len(stack): answer = False

        return answer
