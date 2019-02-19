def isValid(self, s: 'str') -> 'bool':
    stack = []
    check1 = ['{', '(', '[']
    check2 = ['}', ')', ']']

    for i in s:
        # i가 check1에 있다면 스택에 추가
        if i in check1:
            stack.append(i)
        # 첫 i 가 check1에 없으면 당연히 false
        elif stack == []:
            return False
        # i와 같은
        else:
            # 닫는 괄호인데, 스택 LI 와 index 숫자가 다르면 false
            index = check2.index(i)
            print(index)
            if stack.pop() != check1[index]: return False

    if stack == []:
        return True
    else:
        return False