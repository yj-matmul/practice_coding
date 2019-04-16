# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)

        #l1, l2의 수를 비교해 작은 수 부터 연결
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            cur = cur.next

        #남은 수 연결
        while l1:
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = ListNode(l2.val)
            l2 = l2.next
            cur = cur.next

        return dummy.next