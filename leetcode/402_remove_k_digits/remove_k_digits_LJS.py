def removeKdigits(self, num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if k >= len(num):
        return '0'
    elif k == 0:
        return num
    else:
        # list로 받아두기
        list_num = list(num)
        # k 만큼 돌아요
        for i in range(k):
            check = 1
            # [j]가 [j+1]보다 크면 빼버리기
            for j in range(len(list_num) - 1):
                if list_num[j] > list_num[j + 1]:
                    list_num.pop(j)
                    check = 0
                    break
            # 못뺐으면 맨 뒤에꺼 빼기
            if check == 1:
                list_num.pop()

            num = str(int(''.join(list_num)))

    return num