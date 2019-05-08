r, c, k = map(int, input().split())
a = [[0]*101 for _ in range(101)]
n, m = 3, 3
check = 0

for i in range(1, 4):
    a[i][1], a[i][2], a[i][3] = map(int, input().split())

for tic in range(101):
    # 맞으면 바로 break 해서 몇 tic 걸렸는지 출력
    if a[r][c] == k:
        print(tic)
        check = 1
        break

    # r연산
    if n >= m:
        for i in range(1, n+1):
            # 등장횟수 받아놓을 공간 (index = 숫자, 실제값 = 등장횟수)
            dp = [0] * 101
            for j in range(1, m+1):
                if a[i][j]:
                    dp[a[i][j]] += 1
                    a[i][j] = 0
            b = []
            for j in range(101):
                if dp[j]:
                    b.append((dp[j], j))
            # 실제값(등장횟수) 기준 소팅
            b.sort()
            # m 길이 정리
            m = max(m, len(b)*2)
            j=1
            for x in b:
                a[i][j+1], a[i][j] = x
                j += 2
    # c연산
    else:
        for j in range(1, m+1):
            dp = [0] * 101
            for i in range(1, n+1):
                if a[i][j]:
                    dp[a[i][j]] += 1
                    a[i][j] = 0
            b=[]
            for i in range(101):
                if dp[i]:
                    b.append((dp[i], i))
            b.sort()
            n = max(n, len(b)*2)
            i = 1
            for x in b:
                a[i+1][j], a[i][j] = x
                i += 2
if check == 0:
    print(-1)