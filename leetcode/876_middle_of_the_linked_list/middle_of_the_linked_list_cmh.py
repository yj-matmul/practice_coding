def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # node를 count 할 변수 생성
    cnt = 0

    # head 복사
    dummy = head

    # node를 count
    while head:
        cnt += 1
        head = head.next

    # node의 수를 2로 나눈 몫 만큼 node를 건너띔
    for cnt in range(cnt // 2):
        dummy = dummy.next

    return dummy
