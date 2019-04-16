class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = self.choose_num(nums, 0, len(nums) - 1, 1)

        return score >= 0

    # recursive를 반복해 모든 경우의 수를 고려
    def choose_num(self, nums, s, e, turn):
        if s == e:  # 시작과 끝이 같아진 경우
            return turn * nums[s]
        # 앞을 선택하고 recursive
        dp1 = turn * nums[s] + self.choose_num(nums, s + 1, e, -turn)
        # 뒤를 선택하고 recursive
        dp2 = turn * nums[e] + self.choose_num(nums, s, e - 1, -turn)

        # turn을 고려해서 점수가 가장 높은 값을 선택
        return turn * max(turn * dp1, turn * dp2)
