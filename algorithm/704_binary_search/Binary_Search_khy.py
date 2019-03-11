class Solution:
    def search(self, nums: List[int], target: int) -> int:
        out = -1
        l = 0
        r = len(nums)

        while l < r:
            mid =(l+r)//2

            if nums[mid] == target:
                out = mid
                break

            elif l != mid:
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            else:
                break

        return out