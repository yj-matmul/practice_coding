# n 개의 방 일렬로
# change = -1; 닫힘
# change = 1; 열림
#
# 게임
# 1라운드: 1의 배수(1, 2, 3, ..., n)인 방은 모두 change * -1 --> (n // 1)번 연산
#               (0, 1, 1, ..., n-1)번째 방
# 2라운드: 2의 배수(2, 4, 6, ..., 2*(n //2))인 방은 모두 change * -1 --> (n //2)번 연산
#               (1, 3, 5, ..., 2*(n // 2) - 1)번째 방
# ...
# k라운드: k의 배수(k, 2k, 3k, ..., k*(n // k) - 1)인 방은 모두 change * -1 --> (n // k)번 연산
# 예를 들어 이렇게 방 상태라고 하면 [1, 1, -1, 1, -1, -1, 1]
# output = 3 --> (리스트를 다 더한 값 + n)/2

T = int(input())
cases = [int(input()) for i in range(T)]

for n in cases:
    room = [-1] * n
    # print('{}개의 방이 있다'.format(n))
    for k in range(1, n + 1):
        # print('{}번째 round'.format(k))
        for i in range(1, n // k + 1):
            # print('{}번 방을 열거나 닫는다'.format(k * i - 1))
            room[k * i - 1] = room[k * i - 1] * -1
    print((sum(room) + n)//2)


# n = 5;
# room = [-1, -1, -1, -1, -1]
# 1round --> [1, 1, 1, 1, 1]
# 2round --> [1, -1, 1, -1, 1]
# 3round --> [1, -1, -1, -1, 1]
# 4round --> [1, -1, -1, 1, 1]
# 5round --> [1, -1, -1, 1, -1]


# 한 숫자의 약수의 개수를 어떻게 셀 수 있을까?
# 2는 2개, 4는 3개, 6은 4개,


