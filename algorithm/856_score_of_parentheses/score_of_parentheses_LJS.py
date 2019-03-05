def scoreOfParentheses(self, S: str) -> int:
    stack = []
    for s in S:
        # ( 요건 싹다 넣어요
        if s == '(':
            stack.append(s)
        else:
            # ) 요 경우일때 pop으로 하나 뺌
            pop = stack.pop()
            # pop이 ( 면 괄호 1개 완성으로 1점
            if pop == '(':
                stack.append(1)
            else:
                # pop이 숫자인 경우 current_sum으로 따로 받아두고
                current_sum = pop
                # (가 나와 2배 하기 전까지 사이 숫자 더해주기
                while stack[-1] != '(':
                    current_sum += stack.pop()
                # ( 뽑으면서 숫자 2배하여 append
                stack.pop()
                stack.append(current_sum * 2)
    return sum(stack)