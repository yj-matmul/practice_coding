# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0

        self.count = 0
        self.counting(root)

        return self.count

    def counting(self, node):
        left_same = 0
        right_same = 0
        if node.left:
            if node.left.val == node.val:
                left_same += 1 + self.counting(node.left)
            else:
                left_same = 0
                self.counting(node.left)
        if node.right:
            if node.right.val == node.val:
                right_same += 1 + self.counting(node.right)
            else:
                right_same = 0
                self.counting(node.right)
        self.count = max(self.count, left_same + right_same)

        return max(left_same, right_same)