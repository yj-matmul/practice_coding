class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 각 brick이 끝나는 지점의 index를 저장
        for n in range(len(wall)):
            for idx in range(1, len(wall[n])):
                wall[n][idx] += wall[n][idx - 1]

        blank = {0: 0}  # 각 열마다 벽돌 사이 개수를 담을 hash
        for n in range(len(wall)):
            # 벽돌 맨 끝은 제외
            for idx in wall[n][:-1]:
                if idx in blank.keys():
                    blank[idx] += 1
                else:
                    blank[idx] = 1

        # 전체 열 중 벽돌 사이가 가장 빈 곳을 담을 변수
        max_blank = max(blank.values())

        # 전체 층에서 벽돌 사이가 가장 많이 빈 곳을 빼줌
        return len(wall) - max_blank
