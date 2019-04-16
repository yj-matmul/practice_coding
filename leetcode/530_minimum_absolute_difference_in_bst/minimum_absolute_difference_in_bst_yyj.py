# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # inorder traversal를 recursive하게 구현
        def inorder(node, nums):
            if node.left is not None:
                inorder(node.left, nums)
            nums.append(node.val)
            if node.right is not None:
                inorder(node.right, nums)

        nums = []  # value를 담을 리스트
        inorder(root, nums)

        answer = abs(nums[1] - nums[0])

        # nums는 이미 sort되어 있으니 순서대로 차이 비교해서 차이 적은 것 선택
        for i in range(1, len(nums) - 1):
            answer = min(answer, abs(nums[i + 1] - nums[i]))

        return answer
