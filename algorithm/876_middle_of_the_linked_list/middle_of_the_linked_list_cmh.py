def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # 답을 담을 list 생성
    answer = []

    # 첫번째 head의 node를 저장
    node = head

    # node가 끝날때까지 반복
    while node != None:
        # node의 val를 answer에 저장
        answer.append(node.val)
        # node를 다음 node로 이동
        node = node.next

    # answer의 반부터 출력
    return (answer[(len(answer) // 2):])
