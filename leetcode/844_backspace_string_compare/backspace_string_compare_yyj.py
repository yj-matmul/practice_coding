class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':
        stack = []

        # S부터 계산
        for char in S:
            if char == '#':
                # stack에 알파벳이 있을 경우만 backspace 적용
                if stack:
                    stack.pop()
                continue
            stack.append(char)

        S = ''.join(stack)
        stack = []  # stack 초기화

        for char in T:
            if char == '#':
                # stack에 알파벳이 있을 경우만 backspace 적용
                if stack:
                    stack.pop()
                continue
            stack.append(char)

        T = ''.join(stack)

        return S == T
