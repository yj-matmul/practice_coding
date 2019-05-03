n = int(input())
road = []
for i in range(n):
    road.append(list(map(int, input().split())))
answer = [[0 for _ in range(n)] for _ in range(n)]

"""
1번째 반복문 - 거쳐가는 정점
2번째 반복문 - 출발하는 정점
3번째 반복문 - 도착하는 정점
"""

def floyd(n, road, answer, check):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i==j) or (i==k) or (j==k): continue
                if road[i][j] == (road[i][k] + road[k][j]):
                    answer[i][j] = 1
                if road[i][j] > (road[i][k] + road[k][j]):
                    print(-1)
                    check = 0
                    return road, answer, check
    return road, answer, check

check = 1
road, answer, check = floyd(n, road, answer, check)
if check:
    result = 0
    for i in range(n):
        for j in range(n):
            if not answer[i][j]:
                result += road[i][j]

    print(result//2)