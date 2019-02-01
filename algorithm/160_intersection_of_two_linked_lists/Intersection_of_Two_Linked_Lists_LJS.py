# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 하드코딩
        if headA is None or headB is None:
            return

        currA = headA
        currB = headB
        # A랑 B 길이 찾기
        lenA = 0
        while currA:
            lenA += 1
            currA = currA.next

        lenB = 0
        while currB:
            lenB += 1
            currB = currB.next

        currA = headA
        currB = headB

        # 길이 똑같이 맞춰주기
        if lenB > lenA:
            count = lenB - lenA
            while count > 0:
                currB = currB.next
                count -= 1

        if lenA > lenB:
            count = lenA - lenB
            while count > 0:
                currA = currA.next
                count -= 1

        # 같은 위치 찾기
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
