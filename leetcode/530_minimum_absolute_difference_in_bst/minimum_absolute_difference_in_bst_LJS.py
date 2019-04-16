# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 풀어서 담을 빈공간
        self.stack = []
        # 풀어서 stack에 오름차순으로 정리
        self.inorder(root)

        # 최소 절대값 선언
        min_abs = abs(self.stack[0] - self.stack[-1])

        for i in range(1, len(self.stack)):
            min_abs = min(min_abs, abs(self.stack[i] - self.stack[i - 1]))

        return min_abs

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        self.stack.append(node.val)
        if node.right:
            self.inorder(node.right)
