class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        answer = 0

        for char in S:
            if char in J: answer += 1

        return answer
