#변수 받기
n_rope = int(input())
list_rope = []
for i in range(n_rope):
    rope = int(input())
    list_rope.append(rope)

list_rope.sort()#순서대로 정렬

dp = 0
for i in range(n_rope):
    temp = list_rope[i]*(n_rope-i) #최소 무게*사용 로프
    if dp <= temp: #맥스값 갱신
        dp = temp

print(dp)