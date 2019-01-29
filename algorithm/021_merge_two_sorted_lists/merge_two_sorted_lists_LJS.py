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
        if l1 == None: return l2
        if l2 == None: return l1

        if l1.val <= l2.val:
            head = ListNode(l1.val)
            l1 = l1.next  # 다음 val로 바꿔준다. l1을
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        currentnode = head

        while (l1 != None) & (l2 != None):
            if l1.val <= l2.val:
                currentnode.next = ListNode(l1.val)
                l1 = l1.next
                currentnode = currentnode.next

            else:
                currentnode.next = ListNode(l2.val)
                l2 = l2.next
                currentnode = currentnode.next

        if l1 != None: currentnode.next = l1
        if l2 != None: currentnode.next = l2

        return head