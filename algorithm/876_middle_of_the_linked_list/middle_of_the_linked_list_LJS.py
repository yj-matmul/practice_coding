# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        # temp = ListNode(None)
        temp = head

        while 1:
            if temp.next == None:
                break
            count += 1
            temp = temp.next

        if count % 2 == 0:
            count = count / 2
        else:
            count = (count / 2) + 1

        for i in range(int(count)):
            head = head.next

        return head