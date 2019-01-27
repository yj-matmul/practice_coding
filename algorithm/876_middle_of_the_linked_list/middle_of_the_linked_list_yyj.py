# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Node의 value를 담을 리스트
        val = []
        val.append(head.val)
        # Node 순대로 value를 담음
        while head.next:
            head = head.next
            val.append(head.val)

        return val[len(val) // 2:]
