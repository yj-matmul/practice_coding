class Solution:
    def backspaceCompare(self, S: 'str', T: 'str') -> 'bool':

        # 변수생성
        check_del = '#'
        check_s = []
        check_t = []

        # S 에 '#'이 없으면 그냥 list 로 반환
        if check_del not in S:
            check_s = list(S)
        else:
            for s in S:
                # '#' 이면 check_s 가장 최근 값 pop
                if s == check_del:
                    if len(check_s) > 0:
                        check_s.pop()
                # '#' 아니면 check_s 에 append
                else:
                    check_s.append(s)
        # 위와 동일
        if check_del not in T:
            check_t = T

        else:
            for t in T:
                if t == check_del:
                    if len(check_t) > 0:
                        check_t.pop()
                else:
                    check_t.append(t)

        return check_s == check_t
