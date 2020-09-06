# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 아무것도 주어지지 않은 경우
        if head is None:
            return head

        nodes = [head]
        while head.next:
            head = head.next
            nodes.append(head)

        head = nodes[-1]
        while nodes:
            node = nodes.pop()
            if nodes:
                node.next = nodes[-1]
            else:
                node.next = None

        return head