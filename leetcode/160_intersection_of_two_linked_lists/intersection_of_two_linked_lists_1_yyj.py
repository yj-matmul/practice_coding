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
        # dummy Node 생성과
        dummyA = headA
        dummyB = headB

        # B의 linked node의 모든 값을 담음
        valueB = []
        while dummyB != None:
            valueB.append(dummyB.val)
            dummyB = dummyB.next

        # value값이 같을 때만 비교
        while dummyA != None:
            if dummyA.val not in valueB:
                pass
            else:
                # dummyB 처음부터 비교
                dummyB = headB
                cnt = 1
                while dummyB != None:
                    if dummyB.val != dummyA.val:
                        dummyB = dummyB.next
                        cnt += 1
                        continue
                    # value가 같아도 노드가 다른 경우 패스
                    elif dummyB != dummyA:
                        if dummyA.val in valueB[cnt:]:
                            dummyB = dummyB.next
                            headB = dummyB
                            continue
                        else:
                            break
                    # 노드가 같은 경우 빠져나옴
                    else:
                        return dummyA
            dummyA = dummyA.next

        return dummyA
