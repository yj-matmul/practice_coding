# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        answer = False
        if not root: return answer
        total = 0
        answer = self.dfs(root, total, answer, target)

        return answer

    def dfs(self, node, total, answer, target):
        total += node.val
        if not node.left and not node.right:
            return total == target

        if node.left:
            answer = self.dfs(node.left, total, answer, target)
            if answer: return answer
        if node.right:
            answer = self.dfs(node.right, total, answer, target)
            if answer: return answer
