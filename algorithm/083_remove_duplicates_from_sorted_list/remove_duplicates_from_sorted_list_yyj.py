# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            # keep: 값이 변하는 노드의 위치를 저장 / curr: 더미 노드
            keep = curr = head

            while curr != None:
                # 마지막 노드에 다가갔을 경우
                if curr.next is None:
                    keep.next = None
                    break
                # 마지막 노드에 없는 경우
                if curr.next.val == curr.val:
                    curr = curr.next
                    continue
                curr = curr.next
                keep.next = curr
                keep = curr

            return head

        # head에 아무것도 없을 경우
        except:
            return head
