def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    try:
        # node를 담을 list 생성
        node_list = []

        # head.next 를 current 로 복사
        current = head.next

        # head의 node를 node_list에 저장
        while current:
            node_list.append(current)
            current = current.next

        # node_list 끝까지 반복
        while node_list:
            # node_list의 맨 끝 node를 head.next로 연결
            head.next = node_list.pop()
            # head를 다음위치로 변경
            head = head.next

            # node_list가 있을때, 맨 앞 node를 head.next로 연결
            if node_list != []:
                head.next = node_list.pop(0)
                # head를 다음위치로 변경
                head = head.next

        # head의 끝을 None으로 연결
        head.next = None

        return

    # head가 None 일때 수행
    except:
        return