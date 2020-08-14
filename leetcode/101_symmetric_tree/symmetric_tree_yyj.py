# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        left = []
        right = []

        if root.left:
            left = self.leftInOrder(root.left, left)
        if root.right:
            right = self.rightInOrder(root.right, right)

        if len(left) != len(right): return False

        for i in range(len(left)):
            if left[i] != right[i]: return False

        return True

    def leftInOrder(self, node, vals):
        vals.append(node.val)
        if node.left:
            vals = self.leftInOrder(node.left, vals)
        else:
            vals.append('null')
        if node.right:
            vals = self.rightInOrder(node.right, vals)
        else:
            vals.append('null')

        return vals

    def rightInOrder(self, node, vals):
        vals.append(node.val)
        if node.right:
            vals = self.rightInOrder(node.right, vals)
        else:
            vals.append('null')
        if node.left:
            vals = self.leftInOrder(node.left, vals)
        else:
            vals.append('null')

        return vals