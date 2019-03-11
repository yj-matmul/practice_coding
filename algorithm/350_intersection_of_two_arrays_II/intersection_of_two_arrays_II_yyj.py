class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        # nums1에서 차례대로 빼기
        for i in nums1:
            # nums2가 존재하고 nums1의 숫자를 가지고 있을때만 실행
            if nums2 and (i in nums2):
                answer.append(i)
                nums2.remove(i)  # 중복을 방지하기 위해

        return answer
