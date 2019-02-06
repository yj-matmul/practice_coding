def findContentChildren(self, g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """

    try:
        answer = 0

        # 오름차순 정렬
        g.sort()
        s.sort()

        # greed를 끝까지 반복
        for greed in g:
            # cookies 가 0 이면 break
            if len(s) == 0:
                break

            # cookie 첫번째가 greed 보다 작으면
            if greed > s[0]:
                # cookie 첫번째가 greed 보다 크고 len(s)가 1이 아닐때까지 pop(0)을 반복
                while (greed > s[0] and len(s) != 1):
                    s.pop(0)

            # greed 가 cookie 첫번째보다 작으면 answer 1증가 후 s.pop(0) = 수행
            if greed <= s[0]:
                answer += 1
                s.pop(0)

        return answer

    # 값이 없을경우 0 을 return
    except:
        return 0
