def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(None)
    dummy.next = head
    curr = dummy

    while curr:
        dup = False
        # next, next.next 가 있고, 그 두개 val 값이 같으면 한칸 패스
        while curr.next and curr.next.next and (curr.next.val == curr.next.next.val):
            curr.next = curr.next.next
            dup = True
        if dup:
            # 같은 값을 다 지워야되니까
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next

# 사실상 while 은 반복 if문