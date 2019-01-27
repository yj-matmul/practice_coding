def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    # 정답 list 생성
    answer = []

    # l1 또는 l2 끝까지 반복
    while l1 != None or l2 != None:
        # l1 끝이 아니면
        if l1 != None:
            # l1 의 값을 answer에 append
            answer.append(l1.val)
            # l1 을 다음 node로 변경
            l1 = l1.next

        # l1과 동일
        if l2 != None:
            answer.append(l2.val)
            l2 = l2.next

    # sort 해 return
    return sorted(answer)
