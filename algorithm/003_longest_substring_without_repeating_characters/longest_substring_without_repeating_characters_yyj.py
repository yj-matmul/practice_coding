class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = []
        # 리스트 길이가 2보다 작은 경우 대비
        if len(s) in [0, 1]:
            answer.append(len(s))
        else:
            start, end = 0, 1
            substring = s[start]
            while end < len(s):
                # 부분 문자열에 있는 값을 만나는 경우 겹치는 문자까지 초기화
                if s[end] in substring:
                    answer.append(len(substring))
                    start += substring.index(s[end]) + 1
                end += 1
                substring = s[start:end]
            # 리스트의 마지막을 만났을 경우 부분 문자열에 추가
            answer.append(len(substring))

        return max(answer)
