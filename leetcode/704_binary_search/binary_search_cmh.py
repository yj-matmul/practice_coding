class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 변수설정, 여기서 answer 는 -1(반복문 후 answer 값 변경 없을때)
        answer = -1
        left = 0
        right = len(nums) - 1

        # 끝까지 탐색
        while left <= right:
            # 중앙 인덱스 설정
            mid = (left + right) // 2

            # nums[mid]값이 target 보다 작으면 left 값을 mid + 1로 변경
            if nums[mid] < target:
                left = mid + 1
            # 반대인경우 right 값을 mid - 1 로 변경
            elif nums[mid] > target:
                right = mid - 1
            # 위의 2가지 제외하면 mid 값이 target 이랑 일치하는 경우 이므로 answer에 mid 저장 후 break
            else:
                answer = mid
                break

        return answer
