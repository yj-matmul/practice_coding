def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    import copy

    # ListNode 생성
    dummy = current = ListNode(0)

    # l1과 l2가 있으면 값비교
    while l1 and l2:

        # l1과 l2값 중 작은 값의 ListNode를 생성해 저장
        if l1.val <= l2.val:
            current.next = ListNode(l1.val)
            l1 = l1.next
        else:
            current.next = ListNode(l2.val)
            l2 = l2.next

        # current를 다음 node로 변경
        current = current.next

    # l1과 l2중 node가 남아있는것을 remain 으로 받음
    if l1 == None:
        remain = l2
    else:
        remain = l1

    # remain을 current에 끝까지 저장
    while remain:
        current.next = remain
        remain = remain.next
        current = current.next

    return dummy.next
