#매트릭스 정보 받기*셋팅
matinfo = list(map(int, input().split()))
mat = [[[0, 0] for i in range(matinfo[1])] for i in range(matinfo[0])]

# 상어 정보 받아서 배치
shark = []
for i in range(matinfo[2]):
    shark.append(list(map(int, input().split())))
    r, c = shark[i][0] - 1, shark[i][1] - 1
    mat[r][c] = [i + 1, shark[i][4]]

#매트릭스 배치하는 함수
def mtmch(mat, r, c, shark, idx):
    r, c = r - 1, c - 1
    idxtemp = mat[r][c][0]
    if mat[r][c][1] < shark[idx][4]:
        mat[r][c] = [idx + 1, shark[idx][4]]
        if idxtemp > 0:
            shark[idxtemp - 1] = [0, 0, 0, 0, 0]

    else:
        shark[idx] = [0, 0, 0, 0, 0]

    return mat, shark


count = 0
for i in range(matinfo[1]): #컬럼 갯수만큼 움직인다
    for j in range(matinfo[0]): #가장 가까이 있는 물고기 낚시
        if mat[j][i][1] > 0:
            count += mat[j][i][1]
            shark[mat[j][i][0] - 1] = [0, 0, 0, 0, 0]
            break
    mat = [[[0, 0] for i in range(matinfo[1])] for i in range(matinfo[0])] #매트릭스 초기화

    #상어 움직임
    for sh in range(len(shark)):
        if shark[sh][0] == 0: #상어 빈곳 패스
            pass
        else:
            if shark[sh][3] == 1:
                mv = (shark[sh][2] - shark[sh][0] + 1) % (matinfo[0] * 2 - 2) #0번째 로우로 옮길 경우 움직일 거리
                shark[sh][0] = matinfo[0] - abs(mv - matinfo[0] + 1) #움직인 후 인덱스
                if (mv - matinfo[0] + 1) <= 0: #방향전환
                    shark[sh][3] = 2
                mat, shark = mtmch(mat, shark[sh][0], shark[sh][1], shark, sh) #매트릭스에 배치

            elif shark[sh][3] == 2:
                mv = (shark[sh][2] + shark[sh][0] - 1) % (matinfo[0] * 2 - 2)
                shark[sh][0] = matinfo[0] - abs(mv - matinfo[0] + 1)
                if (mv - matinfo[0] + 1) > 0:
                    shark[sh][3] = 1
                mat, shark = mtmch(mat, shark[sh][0], shark[sh][1], shark, sh)

            elif shark[sh][3] == 4:
                mv = (shark[sh][2] - shark[sh][1] + 1) % (matinfo[1] * 2 - 2)
                shark[sh][1] = matinfo[1] - abs(mv - matinfo[1] + 1)
                if (mv - matinfo[1] + 1) <= 0:
                    shark[sh][3] = 3
                mat, shark = mtmch(mat, shark[sh][0], shark[sh][1], shark, sh)

            elif shark[sh][3] == 3:
                mv = (shark[sh][2] + shark[sh][1] - 1) % (matinfo[1] * 2 - 2)
                shark[sh][1] = matinfo[1] - abs(mv - matinfo[1] + 1)
                if (mv - matinfo[1] + 1) > 0:
                    shark[sh][3] = 4
                mat, shark = mtmch(mat, shark[sh][0], shark[sh][1], shark, sh)

print(count)