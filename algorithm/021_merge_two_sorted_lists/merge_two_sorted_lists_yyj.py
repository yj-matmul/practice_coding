# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 노드의 값들을 담을 리스트
        vals = []

        while l1 or l2:
            # 한 링크 노드가 끝났을 때
            if l1 is None:
                vals.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                vals.append(l1.val)
                l1 = l1.next
            # 두 링크 노드의 값들이 존재할 때 크기 비교
            else:
                if l1.val >= l2.val:
                    vals.append(l2.val)
                    l2 = l2.next
                else:
                    vals.append(l1.val)
                    l1 = l1.next

        return vals
