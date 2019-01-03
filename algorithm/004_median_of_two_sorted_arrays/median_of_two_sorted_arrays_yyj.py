class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        print(nums1 + nums2)
        while True:
            if len(nums1) == 0:
                for num in nums2:
                    nums.append(num)
                break
            if len(nums2) == 0:
                for num in nums1:
                    nums.append(num)
                break
            if nums1[0] <= nums2[0]:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))

        length = len(nums)
        if length % 2:
            result = nums[length // 2]
        else:
            result = (nums[length // 2 - 1] + nums[length // 2]) / 2

        return result


class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 두 리스트를 합침
        nums = nums1 + nums2
        nums.sort()

        # 리스트 길이에 따라 중앙값 구하는 경우가 달라짐
        length = len(nums)
        if length % 2:
            result = nums[length // 2]
        else:
            result = (nums[length // 2 - 1] + nums[length // 2]) / 2

        return result
