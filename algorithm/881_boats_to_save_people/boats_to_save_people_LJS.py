def numRescueBoats(self, people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    # people.sort(reverse=True)
    # temp = []
    #         x=0
    people.sort()
    count = 0

    #         for _ in range(len(people)):
    #             x=people.pop()
    #             if x<limit:
    #                 temp.append(x)
    #             else:
    #                 people.append(x)
    #                 break

    front = 0
    back = len(people) - 1

    while front <= back:
        count += 1
        if people[front] + people[back] <= limit:
            front += 1
        back -= 1

    # count += len(people)

    return count