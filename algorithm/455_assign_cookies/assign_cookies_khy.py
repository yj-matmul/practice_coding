class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        for i in g:
            for k in s:
                if k >= i:
                    count += 1
                    s.remove(k)
                    # print(count, s)
                    break

        return count