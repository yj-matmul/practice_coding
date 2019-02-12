def lemonadeChange(self, bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    five_count = 0
    ten_count = 0

    for i in range(len(bills)):
        # 5불 경우
        if bills[i] == 5:
            five_count += 1
        # 10불 경우
        elif bills[i] == 10:
            ten_count += 1
            if five_count == 0:
                return False
            five_count -= 1
        # 20불 경우
        else:
            if ten_count >= 1 and five_count >= 1:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                five_count -= 3
            else:
                return False

    return True