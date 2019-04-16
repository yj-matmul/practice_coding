class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        if len(nums1) > len(nums2): #더 긴 리스트를 nums로 지정
            target = nums2
            nums = nums1
        else:
            target = nums1
            nums = nums2

        outlist = []
        l = 0

        for t in target: #target 리스트 값 하나하나 찾기
            r = len(nums)

            while l < r: #binary search 활용
                mid = (l+r)//2

                if nums[mid] == t:
                    outlist.append(t)
                    nums.pop(mid)
                    break

                elif l != mid:
                    if nums[mid] < t:
                        l = mid
                    else:
                        r = mid
                else:
                    break

        return outlist