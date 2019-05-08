N = int(input())
# 정답변수 및 빈 N*N 2차원 배열 생성
answer = 0
dis = [[0 for j in range(N)] for i in range(N)]
tmp = [[0 for j in range(N)] for i in range(N)]

# 위치와 거리값 넣어주기
for i in range(N):
    city_time = list(map(int, input().split()))
    for j in range(N):
        dis[i][j] = city_time[j]
        tmp[i][j] = city_time[j]

for k in range(N):
    # answer 가 -1 이면 break
    if answer == -1:
        break

    for i in range(N):
        # answer 가 -1 이면 break
        if answer == -1:
            break

        for j in range(N):
            # 경유가 아닐경우 continue
            if (i == k) or (j == k):
                continue
            # 문제에서 최단거리값이 모순일 경우 answer = -1 로 변경 후 break
            if dis[i][j] > dis[i][k] + dis[k][j]:
                answer = -1
                break
            # i부터 j까지의 거리가 k를 경유해서 간경우 i부터 j까지 거리 삭제
            if dis[i][j] == dis[i][k] + dis[k][j]:
                tmp[i][j] = 0

# answer 가 -1이 아니면 tmp 행렬에 있는 모든 time 을 더해준 후 2로 나눠준값을 answer 로 저장
if answer != -1:
    for time in tmp:
        answer += sum(time)
    answer = int(answer/2)

print(answer)
