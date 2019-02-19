def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
    #         stack = []
    #         result = [0] * len(T)

    #         for i in range(len(T)):
    #             if len(stack)== 0:
    #                 stack.append((i,T[i]))
    #             else:
    #                 flag = True
    #                 while len(stack)>0 and flag:
    #                     # 현재 온도가 스택보다 높으면 if문 들어감
    #                     if stack[-1][1] < T[i]:
    #                         temp = stack.pop()
    #                         #result[last_index] = 현재 index - last index
    #                         result[temp[0]]= i-temp[0]
    #                     else:
    #                         flag=False
    #                 stack.append((i,T[i]))
    #         return result

    if not T:
        return []

    result = [0] * len(T)
    stack = []

    for curr_idx, curr_temp in enumerate(T):

        while stack and curr_temp > stack[-1][1]:
            last_idx, last_temp = stack.pop()
            result[last_idx] = curr_idx - last_idx

        stack.append((curr_idx, curr_temp))

    return result