def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """

    # input 이 없을경우 종료
    if head == None:
        return

    # 값을 받을 리스트 생성
    node_list = []

    # head 복사
    current = current_2 = head

    # head 의 끝까지 반복해 node의 값을 node_list에 저장
    while current.next:
        current = current.next
        node_list.append(current)

        # node_list 끝까지 반복
    while (node_list):
        # current_2.next의 값을 node_list의 맨뒤를 pop 후 val의 값을 저장
        current_2.next = ListNode(node_list.pop().val)

        # node_list의 값이 존재하면 수행
        if node_list != []:
            # current_2.next의 값을 node_list의 맨앞을 pop 후 val의 값을 저장
            current_2.next.next = ListNode(node_list.pop(0).val)
            # current_2 를 current_2.next.next 로 저장
            current_2 = current_2.next.next
