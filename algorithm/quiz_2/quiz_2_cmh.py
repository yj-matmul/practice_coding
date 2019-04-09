"""
quiz 2
주어진 문자열을 이용해 가장 다양한 종류의 음식을 먹은 사람을 구하시오.
단, 여러 사람일 경우 알파벳 순서대로 정렬해서 사람의 목록을 반환하시오.

예시
foods = ['alex pizza rice hamburger', 'bob pasta salad', 'alex rice noodle', 'tom salad rice pizza meat']

alex는 pizza, rice, hamburger, noodle 4가지 종류
bob은 pasta, salad 2가지 종류
tom은 salad, rice, pizza, meat 4가지 종류

가장 다양한 종류의 음식을 먹은 사람은 alex와 tom이고
이름을 알파벳 순으로 정렬하면 alex가 앞에 온다.

정답: ['alex', 'tom']

"""


def quiz2(foods):
    food_dict = {}
    cnt = 0

    for food in foods:
        temp = food.split()

        if temp[0] in food_dict:
            food_dict[temp[0]].extend(temp[1:])
        else:
            food_dict[temp[0]] = temp[1:]

    name = list(food_dict.keys())
    have = list(food_dict.values())
    answer = []

    for x in range(len(have)):

        if len(set(have[x])) > cnt:
            answer = []
            answer.append(name[x])
            cnt = len(set(have[x]))

        elif len(set(have[x])) == cnt:
            answer.append(name[x])

    answer.sort()

    return print(answer)


foods = ['tom salad rice pizza meat', 'alex pizza rice hamburger', 'bob pasta salad', 'alex rice noodle']

quiz2(foods)
