class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # 사람을 무게 순으로 정렬
        people.sort()

        # 필요한 보트 수
        boat = 0

        while len(people) > 1:
            # 가장 가벼운 사람과 무거운 사람의 무게가 조건에 족하면 2사람을 제외
            if people[0] + people[-1] <= limit:
                people.pop(0)
            people.pop()
            boat += 1

        # 1명만 남았을 경우 보트 하나 추가
        if len(people) > 0: boat += 1

        return boat
