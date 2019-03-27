# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.stack = []
        self.traversal(root, '')

        return self.stack

    def traversal(self, node, path):
        if not node: return None

        if not node.left and not node.right:
            self.stack.append(path + str(node.val))

        self.traversal(node.left, path + str(node.val) + '->')
        self.traversal(node.right, path + str(node.val) + '->')