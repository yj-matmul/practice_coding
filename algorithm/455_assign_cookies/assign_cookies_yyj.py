class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 만족한 아이들의 수
        num = 0

        # 아이나 쿠키가 없을 경우
        if len(g) * len(s) == 0: return num

        # 각 리스트 정렬
        g.sort()
        s.sort()

        # g의 최소값이 s의 최대값보다 크면 비교가 필요없음
        if g[0] > s[-1]: return num

        for n in range(len(g)):
            # 쿠키가 다 떨어졌을 경우
            if len(s) == 0: break
            # 가장 큰 쿠키를 원하는 아이가 만족할 때
            if g[-1] <= s[-1]:
                num += 1
                g.pop()
                s.pop()
            # 만족 못 할 경우 다음 아이로 넘어감
            else:
                g.pop()

        return num
