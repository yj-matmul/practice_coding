def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root: return []

    stack = []
    self.inorder(root, stack)

    return stack


def inorder(self, node, stack):
    if node.left:
        self.inorder(node.left, stack)
    stack.append(node.val)
    if node.right:
        self.inorder(node.right, stack)