def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # head 복사
    dummy = current = head

    # node의 val를 받을 list 생성
    val_list = []

    # head 끝까지 반복
    while head:
        # val_list에 node의 val을 저장
        val_list.append(head.val)
        # node를 다음 node로 변경
        head = head.next

    # node의 val을 역순으로 저장
    for i in range(1, len(val_list) + 1):
        current.val = val_list[-i]
        current = current.next

    return (dummy)
