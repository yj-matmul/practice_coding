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
        listnum = []
        dummy = cur = ListNode(0)
        dummy.next = head

        #리스트로 담기
        while head:
            print(head.val)
            listnum.append(head.val)
            head = head.next
        #가운데 수 구하기
        idx = (len(listnum) // 2) + 1

        #가운데 링크드 리스트 호출
        head = dummy
        for i in range(idx):
            cur.next = head.next
            head = head.next

        return cur.next