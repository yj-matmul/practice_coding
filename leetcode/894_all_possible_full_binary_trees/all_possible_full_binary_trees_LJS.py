class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            for j in self.allPossibleFBT(i):
                for k in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = j
                    root.right = k
                    res.append(root)
        return res