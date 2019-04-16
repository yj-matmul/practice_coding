class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = 0
        x2 = 0

        while l1:
            x1 = x1 * 10 + l1.val
            l1 = l1.next

        while l2:
            x2 = x2 * 10 + l2.val
            l2 = l2.next

        x = x1 + x2

        dummy = ListNode(0)
        curr = dummy

        for i in str(x):
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        return curr.next