"""
quiz 3
각 스킬을 배우기 위한 스킬 포인트를 구하시오.

상위 스킬을 배우기 위해서는 하위 스킬을 배워야 한다

예시는 이중리스트 구조
[[상위 스킬, 하위 스킬], [상위 스킬, 하위 스킬], ...], 모든 스킬을 찍기 위한 스킬포인트

예시
total_sp = 121
skills = [[1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
1 스킬은 2, 3 스킬을 배워야 사용 가능
3 스킬은 4, 5, 6 스킬을 배워야 사용 가능

2, 4, 5, 6 스킬은 자신보다 하위 스킬이 없다
1, 3은 자신보다 하위 스킬이 존재
1스킬: 44point, 2스킬: 11point, 3스킬: 33point, 4스킬: 11point, 5스킬: 11point, 6스킬: 11point

스킬의 상하관계 그림은 카톡방의 사진을 참고하세요.

정답: answer = [44, 11, 33, 11, 11, 11]

다른 예시도 실행해보세요
total_sp = 20
skills = [[1, 2], [1, 3], [3, 4], [3, 5], [3, 6], [4, 7], [4, 8], [4, 9]]
answer = [6, 1, 5, 3, 1, 1, 1, 1, 1]
"""

total_sp = 121
skills = [[1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
# answer = [44, 11, 33, 11, 11, 11]

sk_temp = []
sk_temp_2 = []

for skill in skills:
    sk_temp.append(skill[0])
    sk_temp_2.append(skill[1])


print(sk_temp)
print(sk_temp_2)
sk_up = list(set(sk_temp))

answer = [1] * max(sk_temp_2)

for x in sk_up:
    answer[x-1] = 0

print(answer)

while 0 not in answer:
    for x in range(len(sk_temp_2)):
        check = sk_temp[x]








#def quiz3(skills, total_sp):
#quiz3(skills, total_sp)


