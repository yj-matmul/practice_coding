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

        return self.deepCopy(head, RandomListNode(0))

    def deepCopy(self, origin, copy):
        if origin == None:
            return None

        copy.label = origin.label
        if origin.random:
            copy.random = RandomListNode(origin.random.label)
        copy.next = self.deepCopy(origin.next, RandomListNode(0))

        return copy