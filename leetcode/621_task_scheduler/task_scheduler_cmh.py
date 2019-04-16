class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':

        try:
            # 변수들 생성
            answer = 0
            q_task = [0] * n
            end_task = []
            dic_task = {}

            # task dic 생성
            for task in tasks:
                if task in dic_task:
                    dic_task[task] += 1
                else:
                    dic_task[task] = 1

            # dic 정렬
            dic_task = sorted(dic_task.items())

            while True:
                # flag 는 'idle' 유무 판단
                flag = True

                # dic 을 task 의 숫자로 정렬
                dic_task.sort(key=lambda element: element[1], reverse=True)

                for x in range(len(dic_task)):
                    # x 가 n 보다 크면 다시 처음부터 시작
                    if x > n:
                        flag = False
                        break

                    # q_task 에 해당 task 가 없는 경우 q_task 에서 가장 처음 들어온 task 를 pop 하고 새로운 task 를 append
                    if dic_task[x][0] not in q_task:
                        q_task.pop(0)
                        q_task.append(dic_task[x][0])
                        dic_task[x] = (dic_task[x][0], dic_task[x][1] - 1)
                        answer += 1
                        flag = False

                    # dic 의 task 값이 0 이면 해당 task 는 end_task 로 append
                    if dic_task[x][1] == 0:
                        end_task.append(x)

                # end_task 의 dic 들을 모두 pop
                while end_task:
                    dic_task.pop(end_task.pop())

                # task 가 모두 끝났을때 break
                if dic_task == []:
                    break

                # flag 가 참이면 실행
                if flag:
                    answer += 1
                    q_task.pop(0)
                    q_task.append('idle')

        except:
            answer = len(tasks)

        return answer
