"""
quiz 1
과속 방지 카메라의 위치와 도착시간을 이용해 구간별 과속 횟수를 구하시오

[[카메라 위치, 도착까지 걸린 누적 시간]], 제한 속도
예시
[[60, 1], [150,2]], 제한속도 60

시작 위치는 0, 시작 시간은 0에서 시작한다.
1. 0~60 까지 1시간 만에 도착했으므로 평균 속도는 60
  제한 속도를 넘지 않았으므로 과속 횟수 = 0
2. 60~150 까지 1시간 만에 도착했으므로  평균속도는 90
  제한 속도 60을 넘었으므로 과속 횟수 = 1

정답: 과속횟수는 1

"""


def quiz1(limit_speed, cameras):
    dis = 0
    time = 0
    answer = 0

    for step in cameras:
        if (step[0] - dis) / (step[1] - time) > limit_speed:
            answer += 1

        dis = step[0]
        time = step[1]

    return print(answer)


cameras = [[60, 1], [150, 2]]
limit_speed = 60

quiz1(limit_speed, cameras)
