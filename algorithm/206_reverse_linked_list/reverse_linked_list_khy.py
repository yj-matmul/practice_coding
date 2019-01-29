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
        dummy = cur = ListNode(0)
        listnum = []

        #풀어서 리스트에 담기
        while head:
            print(head.val)
            listnum.append(head.val)
            head = head.next
        #거꾸로 링크드 리스트로 만들기
        for i in listnum[::-1]:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next