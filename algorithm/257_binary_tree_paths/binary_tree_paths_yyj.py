# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []  # 모든 root-to-leaf path 를 담음

        # root가 None일 경우
        if not root: return ans

        stack = []  # 백트래킹을 위한 메모리
        path = []  # value를 저장 (str)
        past_nodes = [root]  # 지나온 노드를 모두 저장할 리스트
        curr = root  # 현재 노드

        while True:
            # 왼쪽 자식 노드가 있고 이미 지난 노드가 아닌 경우
            if (curr.left) and (curr.left not in past_nodes):
                stack.append(curr)
                past_nodes.append(curr)
                path.append(str(curr.val))  # join 함수를 위해 str 타입 변경
                curr = curr.left
                continue

            # 오른쪽 자식 노드가 있고 이미 지난 노드가 아닌 경우
            if (curr.right) and (curr.right not in past_nodes):
                stack.append(curr)
                past_nodes.append(curr)
                path.append(str(curr.val))  # join 함수를 위해 str 타입 변경
                curr = curr.right
                continue

            # 자식 노드가 없는 leat node 일 경우
            if (not curr.left) and (not curr.right):
                past_nodes.append(curr)
                path.append(str(curr.val))  # join 함수를 위해 str 타입 변경
                # ans에 root-to-leaf path 추가
                ans.append('->'.join(path))
                path.pop()

            # stack이 없으면 모든 경로를 다 체크함
            if not stack: break

            # 백트래킹하고 path의 최근 값 제외
            curr = stack.pop()
            path.pop()

        return ans
