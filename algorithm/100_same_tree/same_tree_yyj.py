# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_vals = self.levelOrder(p)  # p root의 value들을 list에 담음
        q_vals = self.levelOrder(q)  # q root의 value들을 list에 담음

        return p_vals == q_vals  # 두 리스트의 일치 여부

    # 레벨(깊이) 단위로 node를 저장
    def levelOrder(self, node):
        q = [node]  # queue 개념을 이용
        vals = []  # 각 node의 value를 담는 리스트

        while q:
            curr = q.pop(0)  # 앞에서부터 뽑아냄
            # node가 존재하면 value를 뽑고 자식 노드들을 q에 저장
            if curr:
                vals.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            # node가 존재하지 않으면 null값을 넣고 자식노드 패스
            else:
                vals.append(None)

        return vals
