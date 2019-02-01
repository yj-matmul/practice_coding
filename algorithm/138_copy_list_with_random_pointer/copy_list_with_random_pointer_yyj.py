# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        try:
            # deepcopy를 위해 Node 새로 생성
            curr, clone = head, RandomListNode(head.label)

            # 이 노드의 next가 copy list의 head를 가르칠 거임
            dummyHead = RandomListNode(0)
            dummyHead.next = clone

            # 노드의 끝에 닿으면 빠져나옴
            while curr != None:
                # 현재 Node의 random pointer가 있을 때만 작동
                if curr.random:
                    currRandom = curr.random
                    dummyRandom = RandomListNode(currRandom.label)
                    clone.random = dummyRandom
                # 현재 Node의 next pointer가 있을 때만 작동
                if curr.next:
                    currNext = curr.next
                    dummyNext = RandomListNode(currNext.label)
                    clone.next = dummyNext
                # 노드를 각각 옮김
                curr = curr.next
                clone = clone.next

            return dummyHead.next

        # head가 아무것도 없을 경우
        except:
            return None
