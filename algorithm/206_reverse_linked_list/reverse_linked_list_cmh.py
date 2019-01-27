def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # 정답 list 생성
    answer = []

    # node의 값을 head 로 생성
    node = head

    # node의 끝까지 반복
    while node != None:
        # node의 값을 append
        answer.append(node.val)
        # node 를 다음 node로 변경
        node = node.next

    # 역순으로 리스트 출력
    return answer[::-1]
