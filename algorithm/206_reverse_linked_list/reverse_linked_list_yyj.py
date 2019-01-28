# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 아무것도 주어지지 않은 경우
        if head is None:
            return []
        # Node의 value를 담는 과정
        values = []
        values.append(head.val)
        while head.next:
            head = head.next
            values.insert(0, head.val)

        return values
