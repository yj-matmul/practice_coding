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
                # 노드의 값이 반복될 때 curr만 다음으로 이동
                if keep.val == curr.val:
                    curr = curr.next
                    continue
                # 노드의 값이 반복되지 않을 때 keep에 마지막으로 반복된 노드를 할당
                keep.next = curr
                keep = curr
                curr = curr.next
            # 노드의 끝을 None으로 연결
            keep.next = curr

            return head

        # head에 아무것도 없을 경우
        except:
            return head
