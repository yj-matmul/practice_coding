class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        stack = [0]  # 처음 단계 반영

        for n in S:
            # 차원을 높임
            if n == '(':
                stack.append(0)
            else:
                tmp = stack.pop()
                # 곱하기인지 더하기인지 자연스럽게 구분
                stack[-1] += max(2 * tmp, 1)

        return stack.pop()
