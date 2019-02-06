def lemonadeChange(self, bills):
    """
    :type bills: List[int]
    :rtype: bool
    """

    # 잔돈 및 정답 변수 설정
    change_5 = 0
    change_10 = 0
    answer = True

    # bills list 반복
    for bill in bills:
        # bill이 5인경우 change_5 1 증가
        if bill == 5:
            change_5 += 1

        # bill이 10이고 change_5가 1이상인경우 change_10을 1 증가시키고 change_5를 1 감소시킴
        elif bill == 10 and change_5 >= 1:
            change_10 += 1
            change_5 -= 1

        # bill이 20 이고 change_5가 3이상이거나 change_5가 1이상이고 change_10이 1이상인 경우
        elif bill == 20 and (change_5 >= 3 or (change_5 >= 1 and change_10 >= 1)):
            # change_10이 1이상인 경우에는 change_5, change_10을 1 감소시킴
            if change_10 >= 1:
                change_5 -= 1
                change_10 -= 1
            # change_5를 3 감소시킴
            else:
                change_5 -= 3

        # 이외에는 answer = False 변경 후 break
        else:
            answer = False
            break

    return answer
