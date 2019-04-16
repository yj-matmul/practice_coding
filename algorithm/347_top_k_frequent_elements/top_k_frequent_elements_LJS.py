class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}

        # 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리하다.
        for i in nums:
            dict_nums[i] = dict_nums.get(i, 0) + 1

        items_nums = list(dict_nums.items())

        items_nums.sort(key=lambda value: value[1], reverse=True)

        result = []
        i = 0
        while k:
            result.append(items_nums[i][0])
            i += 1
            k -= 1

        return result