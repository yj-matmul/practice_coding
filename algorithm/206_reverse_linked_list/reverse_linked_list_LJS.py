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
        if not head or not head.next:
            return head

        current_node, pointer = head, head.next
        current_node.next = None

        while pointer:
            temp = pointer.next  # temp = 3,4,5,null
            pointer.next = current_node  # 2 뒤에 1,null 로 가라
            current_node, pointer = pointer, temp  # pointer 는 2,1,null temp는 3,4,5,null

        return current_node