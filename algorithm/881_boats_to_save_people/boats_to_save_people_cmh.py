def numRescueBoats(self, people: 'List[int]', limit: 'int') -> 'int':
    answer = 0
    people.sort()

    while len(people) >= 2:
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop()
            answer += 1
        else:
            people.pop()
            answer += 1

    if people:
        answer += 1

    return answer
