r, c, m = map(int, input().split())
fishtank = [[[0,0,0] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    fishtank[x-1][y-1] = [s, d, z]
answer = 0

def hunt(fishtank,count,answer):
    # 한칸 확인해서 있으면 잡고, [0,0,0] 만들거나
    # 없으면 그냥 그대로 리턴
    for j in range(r):
        _, _, zz = fishtank[j][count]
        if zz:
            answer += zz
            fishtank[j][count] = [0, 0, 0]
            return fishtank, answer
    return fishtank, answer

def one_tick(fishtank):
    # 1초 지난 어항 구현
    # 임시(temp_tank)로 받아두고 실제 어항하고 구분해서 사용
    temp_tank = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
    for row in range(r):
        for col in range(c):
            temp = fishtank[row][col]
            if temp[2] == 0:
                continue
            else:
                if (temp[1] == 1) or (temp[1] == 2):
                    temp_s, temp_d, temp_row = temp[0]% ((r-1)*2), temp[1], row
                    # 상하 무빙시 s가 겁나 크면 아래 for문을 너무 많이 돌아서 터짐
                    # 그래서 (r-1)*2로 나눈 나머지 만큼만 이동하면 같은 결과
                    for _ in range(temp_s):
                        # 어항 벽에 닿으면 turn
                        if temp_row == 0 and temp_d == 1:
                            temp_d = 2
                        if temp_row == r-1 and temp_d == 2:
                            temp_d = 1
                        # 실제 이동
                        if temp_d == 1:
                            temp_row -= 1
                        elif temp_d == 2:
                            temp_row += 1

                    _, _, temp_z = temp_tank[temp_row][col]
                    # 임시어항에 이동 완료한 더 큰 고기 있으면 잡아먹힘
                    # 안잡아 먹혔으면 위치저장
                    if temp[2] > temp_z:
                        temp_tank[temp_row][col] = [temp_s, temp_d, temp[2]]

                elif (temp[1] == 3) or (temp[1] == 4):
                    # 좌우 무빙도 동일
                    temp_s, temp_d, temp_col = temp[0]% ((c-1)*2), temp[1], col
                    for _ in range(temp_s):
                        if temp_col == 0 and temp_d == 4:
                            temp_d = 3
                        if temp_col == c-1 and temp_d == 3:
                            temp_d = 4

                        if temp_d == 3:
                            temp_col += 1
                        elif temp_d == 4:
                            temp_col -= 1

                    _, _, temp_z = temp_tank[row][temp_col]
                    if temp[2] > temp_z:
                        temp_tank[row][temp_col] = [temp_s, temp_d, temp[2]]
                # 고기 이동 완료되면 그 위치 초기화
                fishtank[row][col] = [0,0,0]
    fishtank = temp_tank[:]
    return fishtank

for count in range(c):
    fishtank, answer = hunt(fishtank, count, answer)
    fishtank = one_tick(fishtank)

print(answer)
