# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        depths = []
        depth = 0
        depths = self.InOrder(root, depth, depths)

        return max(depths)

    def InOrder(self, node, depth, depths):
        depth += 1
        depths.append(depth)
        if node.left:
            depths = self.InOrder(node.left, depth, depths)
        if node.right:
            depths = self.InOrder(node.right, depth, depths)

        return depths