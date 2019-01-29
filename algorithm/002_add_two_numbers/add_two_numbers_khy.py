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
        listnum1 = []
        iistnum2 = []
        num1 = num2 = 0
        dummy = cur = ListNode(0)

        #풀어서 리스트에 담기
        while l1:
            listnum1.append(l1.val)
            l1 = l1.next
        while l2:
            iistnum2.append(l2.val)
            l2 = l2.next

        #계산할 숫자로 만들어주기
        for i in range(len(listnum1)):
            num1 += listnum1[i] * (10 ** i)
        for i in range(len(iistnum2)):
            num2 += iistnum2[i] * (10 ** i)
        #더하기
        finalsum = list(str(num1 + num2))

        #다시 링크드 리스트로 변환
        for i in finalsum[::-1]:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next