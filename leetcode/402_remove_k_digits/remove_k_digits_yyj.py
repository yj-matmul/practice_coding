class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 주어진 숫자와 지워야하는 자릿수가 같을 경우 0
        if len(num) == k: return str(0)

        # 주어진 숫자를 리스트화
        nums = list(num)

        # stack: 가장 큰 자리수부터 keep할 숫자를 담음 / n: nums의 인덱스
        stack = [nums[0]]
        n = 1
        while n < len(nums):
            # stack에 아무것도 없을 경우
            if len(stack) == 0:
                # stack에 없는데 비교 숫자가 0인 경우 stack에 추가 안함
                # 그러나 마지막 숫자면 0이라도 stack에 추가
                if (nums[n] != u'0') or (n == len(nums) - 1):
                    stack.append(nums[n])
                n += 1
                continue

            # stack의 끝 숫자가 비교 숫자보다 크면 stack의 끝 숫자를 제외하고 반복
            if (stack[-1] > nums[n]) & (k > 0):
                stack.pop()
                k -= 1
                continue

            # 오름차순인 경우 숫자를 킵
            stack.append(nums[n])
            n += 1

        # nums가 오름차순대로 되어 있는 경우
        while k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack)
