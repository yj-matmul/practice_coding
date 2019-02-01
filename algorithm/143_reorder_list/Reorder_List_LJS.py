# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return None
        dp = []
        dummy = head
        while dummy:
            dp.append(dummy)
            dummy = dummy.next

        for i in range(len(dp) // 2):
            dp[i].next = dp[len(dp) - i - 1]  # dp0.next = dp3     ,     dp1.next = dp2
            dp[len(dp) - i - 1].next = dp[i + 1]  # dp3.next = dp1   ,     dp2.next = dp2

        dp[i + 1].next = None
        head = dp[0]