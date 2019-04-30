N = int(input())
lopes = []
w = 0

for lope in range(N):
    lopes.append(int(input()))

# 오름차순 정렬
lopes.sort()

# w = min(lope) * len(lope)
# w의 max 값 찾기 위해 반복문 실행
for i, lope in enumerate(lopes):
    if lope * (N-i) > w:
        w = lope * (N-i)

print(w)
