class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        stack = []
        prime = 0
        water = 0
        maxstack = 0
        if len(height) <3:
            return water

        for idx, h in enumerate(height):
            if prime < h: #다음 수가 더 큰 경우
                if len(stack)>0: #stack이 비어있지 않으면
                    if stack[-1][1] < h: #stack의 바로 앞 수보다 새로운 수가 큰 경우
                        fl = 1
                        while fl == 1: #필요없는 부분 빼주기
                            if stack[-1][1]> h or stack[-1][1] == maxstack:
                                fl = 0
                            else:
                                stack.pop()

                stack.append((idx, h))

            prime = h
            maxstack = max(h, maxstack)

        for s in range(1, len(stack)): #넓이 계산
            hght = min(stack[s-1][1], stack[s][1])
            wdth = stack[s][0] - stack[s-1][0] -1
            block = height[(stack[s-1][0]+1):stack[s][0]]
            block = list(map(lambda x: min(x, hght), block))
            water += hght*wdth - sum(block)
        return water