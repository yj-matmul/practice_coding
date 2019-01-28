def pushDominoes(self, dominoes):
    """
    :type dominoes: str
    :rtype: str
    """

    # 변수들 지정
    answer = ''
    left = '.'
    left_num = 0

    # input 값 list로 변경
    domino = list(dominoes)

    # input 값 끝까지 반복
    for i in range(len(domino)):

        # '.' 일때 찾기
        if domino[i] == '.':

            # '.' 일때 while flag True 변경 및 index 저장
            flag = True
            check = i

            # '.'이 아닌 right 값 찾기
            while flag:
                check += 1

                # list 끝이면 while 종료
                if check == len(domino):
                    right = '.'
                    flag = False

                # '.' 아닌 값을 찾았으면 index 저장 후 while 종료
                elif domino[check] != '.':
                    right = domino[check]
                    right_num = check
                    flag = False

             # left 와 right 가 같으면 left or right 값
            if left == right:
                answer += right

            # left or right 가 '.' 이면
            elif left == '.' or right == '.':
                if right == 'L':
                    answer += right
                elif left == 'R':
                    answer += left
                else:
                    answer += '.'

            # 그밖에 left 와 right 값이 다른경우
            else:
                if left == 'L':
                    answer += '.'

                # left = R, right = L 인 경우
                else:
                    # 현재 위치에서 떨어진 정도를 계산한 check_num 생성
                    check_num = (i - left_num) - (right_num - i)

                    if check_num < 0:
                        answer += left
                    elif check_num > 0:
                        answer += right
                    else:
                        answer += '.'

        # '.' 이 아닐때는 left 값으로 저장 후 answer 에도 추가
        else:
            left = domino[i]
            left_num = i
            answer += domino[i]

    return (answer)
