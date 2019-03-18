# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        dp = []
        self.search(root, dp)
        a = max(dp)
        for i in range(1, len(dp)):
            a = min(a, abs(dp[i] - dp[i - 1]))

        return a

    def search(self, node, dp):

        if node:
            self.search(node.left, dp)
            dp.append(node.val)
            self.search(node.right, dp)
