def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    # 합계와 answer list 생성
    sum = 0
    answer = []

    # 10의 제곱 변수 설정
    square1 = 0
    square2 = 0

    # l1, l2 마지막 node 까지 반복
    while l1 != None or l2 != None:
        # l1 node가 끝이 아니면
        if l1 != None:
            # sum에 해당 값 * 10의 자리수값 더함
            sum += l1.val * (10 ** square1)
            # l1의 10의 제곱 변수 + 1
            square1 += 1
            # l1 node를 다음 노드로 변경
            l1 = l1.next

        # l1 과 동일
        if l2 != None:
            sum += l2.val * (10 ** square2)
            square2 += 1
            l2 = l2.next

    # sum을 string 으로 변경 후 하나씩 answer 에 int로 append
    for _ in str(sum):
        answer.append(int(_))

    # 리스트의 역순으로 answer return
    return answer[::-1]
