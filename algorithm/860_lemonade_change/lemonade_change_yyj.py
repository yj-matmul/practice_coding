class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 결과 담을 변수
        answer = True
        try:
            # num5: 5달러 개수 / num10: 10달러 개수
            num5 = num10 = 0

            for money in bills:
                # 5달러일 경우 5달러 개수 증가
                if money == 5:
                    num5 += 1
                    continue
                # 10달러일 경우 10달러 개수 증가와 5달러 거슬러줌
                elif money == 10:
                    num5 -= 1
                    num10 += 1
                # 20달러일 때 10달러 먼저 거슬러줌
                elif num10 > 0:
                    num10 -= 1
                    num5 -= 1
                # 10달러가 하나도 없는 경우 5달러 3개 거슬러줌
                else:
                    num5 -= 3

                # 매 거래마다 거슬러줄 수 있는 여부를 따짐
                if num5 < 0:
                    answer = False
                    break

            return answer

        # bills 가 없을 경우
        except:
            return answer
