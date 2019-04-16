# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = self.make_num(l1) + self.make_num(l2)

        # 두 값을 더한 결과가 0일 경우 고려
        if not result: return [0]

        dummy = ListNode(result % 10)  # 맨 끝 노드 생성
        while result:
            # 맨 뒤에서부터 linked list 생성해서 연결
            node = ListNode(0)  # 임시 노드
            node.next = dummy
            result //= 10
            node.val = result % 10
            dummy = node

        return dummy.next

    # linked list의 value를 모아 숫자를 만드는 함수
    def make_num(self, node):
        num = 0  # node의 value를 더할 변수

        while node:
            # 자리수를 하나 올리고 다음 노드로 변경
            num = num * 10 + node.val
            node = node.next

        return num
