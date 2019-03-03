class Solution:
    def scoreOfParentheses(self, S: 'str') -> 'int':
        # 변수 생성
        tmp = 0
        open_check = '('
        score_st = []

        for s in S:
            # '(' 면 score_st 에 append
            if s == open_check:
                score_st.append(s)
            # ')' 면 실행
            else:
                # score_st 가장 최근 값이 '(' 실행
                if score_st[-1] == open_check:
                    score_st.pop()
                    score_st.append(1)
                # score_st 가장 최근 값이 '(' 때를 찾음 그 동안 수는 모두 sum
                else:
                    while score_st[-1] != open_check:
                        tmp += score_st.pop()

                    # '(' 을 pop 하고 tmp 를 2배 해준 후 tmp 초기화
                    score_st.pop()
                    score_st.append(tmp * 2)
                    tmp = 0

        return sum(score_st)
