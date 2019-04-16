# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = []

        num = self.makeNum(l1)
        num += self.makeNum(l2)
        string = str(num)

        length = len(string)

        for n in range(length):
            # 첫 노드를 생성할 때
            if n == 0:
                tmp = self.makeNode(int(string[n]))
                answer.append(tmp)
            else:
                tmp = self.makeNode(int(string[n]), tmp)
                answer.append(tmp)

        return answer[-1]

    # 결과값을 각 자리수 마다 노드에 분배
    def makeNode(self, element, nextNode=None):
        node = ListNode(element)
        node.next = nextNode

        return node

    # 노드의 값들을 연결해 숫자 생성
    def makeNum(self, node):
        res = ''
        while True:
            if node.next == None:
                res += str(node.val)
                break
            else:
                res += str(node.val)
                node = node.next

        res = res[::-1]
        res = int(res)

        return res
