T = int(input())

# n 까지의 숫자중 약수의 개수가 홀수이면 최종적으로 문이 열려있다.
# 약수의 개수가 홀수 인 수 = 제곱 수 (약수의 개수 공식 참고)

for t in range(T):
    n = int(input())

    print(int(n**0.5))
