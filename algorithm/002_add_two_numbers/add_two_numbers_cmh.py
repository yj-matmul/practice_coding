def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    # Listnode 생성
    dummy = current = ListNode(0)

    # check 변수 생성
    check = 0

    # l1, l2 끝까지 반복
    while l1 and l2:
        # 올림자리수와 l1 + l2 더한 result 변수 만들기
        result = l1.val + l2.val + check
        # 올림자리수 check 초기화
        check = 0
        # result가 10을 넘는경우
        if result >= 10:
            # check 1 변경
            check = 1
            # result - 10
            result -= 10
            # current의 다음 노드를 result 로 변경
        current.next = ListNode(result)

        # current, l1, l2 모두 다음 노드로 변경
        current = current.next
        l1 = l1.next
        l2 = l2.next

    # l1 이 남았을 경우 위와 같이 반복
    while l1:
        result = l1.val + check
        check = 0

        if result >= 10:
            check = 1
            result -= 10

        current.next = ListNode(result)
        current = current.next
        l1 = l1.next

    # l2 이 남았을 경우 위와 같이 반복
    while l2:
        result = l2.val + check
        check = 0

        if result >= 10:
            check = 1
            result -= 10

        current.next = ListNode(result)
        current = current.next
        l2 = l2.next

    # 마지막 자리수가 올라갈때, 마지막 check 변수로 추가
    if check == 1:
        current.next = ListNode(1)

    return dummy.next

