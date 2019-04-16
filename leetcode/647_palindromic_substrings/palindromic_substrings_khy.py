class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        slength = len(s)
        for i in range(slength):
            start = i
            end = i + 1
            while end < slength + 1:
                temp = s[start:end]
                if temp == temp[::-1]:
                    count += 1
                else:
                    pass
                end += 1

        return count