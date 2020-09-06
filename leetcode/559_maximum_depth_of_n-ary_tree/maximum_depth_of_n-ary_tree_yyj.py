"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0

        queue = deque([root])
        depths = []
        depth = 0

        depths = self.InOrder(root, depth, depths)
        print(depths)
        return max(depths)

    def InOrder(self, node, depth, depths):
        depth += 1
        print(depth)
        depths.append(depth)
        for child in node.children:
            depths = self.InOrder(child, depth, depths)

        return depths