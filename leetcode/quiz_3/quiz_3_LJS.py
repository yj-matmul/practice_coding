total_sp = 20
skills = [[1, 2], [1, 3], [3, 4], [3, 5], [3, 6], [4, 7], [4, 8], [4, 9]]
ans = [44,11,33,11,11,11]

def solution(skills, total_sp):
    nodes = set()
    for skill in skills:
        nodes.add(skill[0])
        nodes.add(skill[1])
    nodes = list(nodes)
    print(nodes)

    dict_tree = {}
    for node in nodes:
        dict_tree[node] = 1
    print(dict_tree)

    for skill in skills:
        temp = dict_tree.get(skill[0])
        dict_tree[skill[0]] = temp+1
    print(dict_tree)

    dict_values = list(dict_tree.values())
    base_sp = total_sp // sum(dict_values)
    print(base_sp)

    dict_values = list(map(lambda x: x-1 if x>1 else x, list(dict_tree.values())))
    print(dict_values)

    result_dict = {}
    count = 0
    for node in nodes:
        result_dict[node] = dict_values[count]
        count += 1
    print(result_dict)

    dict_skill = {}
    for stree in skills:
        if dict_skill.get(stree[0]):
            temp = dict_skill.get(stree[0])
            temp.append(stree[1])
            dict_skill[stree[0]] = temp
        else:
            temp=[]
            temp.append(stree[1])
            dict_skill[stree[0]] = temp
    print(dict_skill)


    dict_skill_keys = list(dict_skill.keys())
    print(dict_skill_keys)

    for keys in dict_skill_keys:
        for i in dict_skill[keys]:
            if i in dict_skill_keys:
                result_dict[keys] += result_dict[i] - 1
    print(result_dict)

    answer = list(map(lambda x: x* base_sp,list(result_dict.values())))
    print(answer)


solution(skills, total_sp)
