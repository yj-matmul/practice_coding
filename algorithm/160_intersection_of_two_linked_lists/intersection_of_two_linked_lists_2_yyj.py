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
        # dummy Node 생성과 linked list 길이
        dummyA, dummyB = headA, headB
        lenA = lenB = 0

        # 각 linked node의 길이를 구함
        while dummyA != None:
            dummyA = dummyA.next
            lenA += 1
        while dummyB != None:
            dummyB = dummyB.next
            lenB += 1

        # 각 dummy 초기화
        dummyA, dummyB = headA, headB

        # 두 linked list 길이의 차이만큼 제외하고 노드 비교
        if lenA >= lenB:
            for _ in range(lenA - lenB):
                dummyA = dummyA.next
        else:
            for _ in range(lenB - lenA):
                dummyB = dummyB.next
        while dummyA != dummyB:
            dummyA = dummyA.next
            dummyB = dummyB.next

        return dummyA
