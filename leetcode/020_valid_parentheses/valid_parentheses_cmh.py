class Solution:
    def isValid(self, s: 'str') -> 'bool':

        # 변수생성
        answer = True
        open_stack = []
        open_list = ['(', '{', '[']
        close_list = [')', '}', ']']

        # 입력값이 짝수가 아니면 False return
        if len(s) % 2 != 0:
            answer = False

        # 입력값이 짝수일때 실행
        else:
            # s 를 끝까지 반복 수행
            for x in s:
                # x 가 open 문자면 open_stack 에 append
                if x in open_list:
                    open_stack.append(x)
                # x 가 close 문자면 실행
                else:
                    # open_stack 이 비어있으면 False return
                    if open_stack == []:
                        answer = False
                        break

                    # open_stack 에서 가장 최근값을 꺼낸 뒤 open_list 에서 index를 찾아 start 할당
                    start = open_list.index(open_stack.pop())
                    # close_list 에서 index를 찾아 end 할당
                    end = close_list.index(x)

                    # start 와 end 가 짝이 맞는지 확인 후 틀리면 False return
                    if start != end:
                        answer = False
                        break

            # 반복을 다 했는데 open_stack 에 값이 남아있으면 False return
            if open_stack != []:
                answer = False

        return answer