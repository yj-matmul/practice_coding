# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def lenlist(lists):
            num = ""
            while lists:
                num = num + str(lists.val)
                lists = lists.next
            return int(num)

        lenl1, lenl2 = lenlist(l1), lenlist(l2)
        sums = lenl1 + lenl2

        dummy = cur = ListNode(0)
        for i in str(sums):
            cur.next = ListNode(int(i))
            cur = cur.next

        return dummy.next