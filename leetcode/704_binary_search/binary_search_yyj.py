class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, target, 0, len(nums) - 1)

    # recursive binary search
    def binary(self, nums, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] < target:
            return self.binary(nums, target, mid + 1, end)
        elif nums[mid] > target:
            return self.binary(nums, target, start, mid - 1)
        else:
            return mid
