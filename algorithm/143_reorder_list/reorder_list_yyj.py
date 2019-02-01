# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        try:
            # linked list의 모든 요소를 담을 리스트
            nodes = []
            dummy = head.next
            # head 다음부터 노드들을 리스트에 담음
            while dummy != None:
                nodes.append(dummy)
                dummy = dummy.next

            # head에 마지막 노드를 연결
            head.next = nodes[-1]

            # nodes의 양끝을 빼면서 link 연결
            while len(nodes) > 1:
                end = nodes.pop()
                start = nodes.pop(0)
                end.next = start
                if len(nodes):
                    # 노드의 개수가 홀수이고 중간에 있는 노드에 닿았을 때
                    if len(nodes) == 1:
                        nodes[-1].next = None
                    start.next = nodes[-1]
                # 노드의 개수가 짝수이고 중간에 있는 노드에 닿았을 때
                else:
                    start.next = None
        # head에 아무것도 없을 때
        except:
            pass
