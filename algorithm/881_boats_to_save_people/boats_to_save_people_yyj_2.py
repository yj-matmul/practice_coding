class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # 사람을 무게 순으로 정렬
        people.sort()

        # boat: 필요한 보트 수 / start: 가벼운 사람을 가리키는 index
        boat = start = 0

        for n in range(len(people) - 1, -1, -1):
            # 가장 가벼운 사람과 무거운 사람의 무게가 조건에 족하면 2사람을 제외
            if people[start] + people[n] <= limit:
                start += 1
            boat += 1

            # start가 n보다 크면 모든 사람을 다 태웠으니 반복문 탈출
            if start >= n: break

        return boat
