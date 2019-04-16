# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        def getTotal(l):
            total = 0
            x = 0
            while l:
                total += l.val * (10 ** x)
                x += 1
                l = l.next

            return total

        total = getTotal(l1) + getTotal(l2)

        # 다시 숫자를 linked list에 넣어주기
        num_string = str(total)[::-1]
        pre = ListNode(None)
        curr = pre

        for n in num_string:
            curr.next = ListNode(int(n))
            curr = curr.next

        return pre.next