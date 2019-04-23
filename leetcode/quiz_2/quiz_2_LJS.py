foods = ['tom salad rice pizza meat','alex pizza rice hamburger', 'bob pasta salad', 'alex rice noodle']

dict_food = {}
for food in foods:
    temp = list(food.split())
    if dict_food.get(temp[0]):
        temp_set = set(dict_food[temp[0]])
        temp_set.update(temp[1:])
        dict_food[temp[0]] = list(temp_set)
    else:
        dict_food[temp[0]] = temp[1:]

keys = list(dict_food.keys())
values = list(map(lambda x: len(x), list(dict_food.values())))

max_num = max(values)
values = list(map(lambda x: 1 if x==max_num else 0, values))

answer = []
for i in range(len(values)):
    if values[i] == 1:
        answer.append(keys[i])

answer.sort()

print(answer)