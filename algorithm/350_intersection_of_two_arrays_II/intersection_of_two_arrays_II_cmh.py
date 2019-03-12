class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 변수생성
        answer = []

        # 크키가 작은 리스트 찾기
        if len(nums1) > len(nums2):
            check_nums = nums2
            check_nums2 = nums1
        else:
            check_nums = nums1
            check_nums2 = nums2

        # 크기가 작은 리스트에서 값이 다른 리스트에 있는지 확인 후 있으면 해당 값을 pop 해 answer 에 append
        for check in check_nums:
            if check in check_nums2:
                answer.append(check_nums2.pop(check_nums2.index(check)))

        return answer
