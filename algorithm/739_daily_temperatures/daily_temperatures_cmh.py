class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        # 변수생성
        answer = [0] * len(T)
        st_val = []
        st_index = []

        # T 를 끝까지 비교
        for x in range(len(T) - 1):

            # T[x] < T[x+1] 보다 작으면 answer 의 현재 index 에 1 을 넣어줌
            if T[x] < T[x + 1]:
                answer[x] = 1

                # st_val[-1] < T[X+1] 작으면 수행
                try:
                    while (st_val[-1] < T[x + 1]):
                        # st_val 가장 최근값 pop
                        st_val.pop()
                        # st_index 가장 최근값의 index를 answer 에 x - index + 1 값을 넣어줌
                        answer[st_index[-1]] = x - st_index[-1] + 1
                        # st_index 가장 최근값 pop
                        st_index.pop()
                except:
                    pass

            # st_val 에 T[x] 값 append, st_index에 현재 index append
            else:
                st_val.append(T[x])
                st_index.append(x)

        return answer
