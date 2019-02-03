def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    # headA 또는 headB 가 None 인 경우 None return
    if headA == None or headB == None:
        return None

    # headA 와 headB 복사
    A_pointer = headA
    B_pointer = headB

    # A_pointer와 B_pointer를 다음 node로 옮기면서 다를때까지 반복
    while A_pointer != B_pointer:
        # pointer 가 None 이면 서로 다른 head 로 현위치를 바꿈
        A_pointer = headB if A_pointer == None else A_pointer.next
        B_pointer = headA if B_pointer == None else B_pointer.next

    return A_pointer
