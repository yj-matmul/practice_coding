# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals: List[Interval]) -> List[int]:
        start = {}
        end = {}
        for i in range(len(intervals)): #딕셔너리로 받아놓기(key: 값, vlaues:인덱스)
            start[intervals[i].start] = i
            if intervals[i].end in end:
                end[intervals[i].end].append(i)
            else:
                end[intervals[i].end] = [i]

        # keyr값(interval)의 값들을 순서대로 정렬
        s_order = list(start.keys())
        e_order = list(end.keys())

        s_order.sort()
        e_order.sort()

        #dp 만들어두기
        dp = [0 for i in range(len(intervals))]
        l = 0

        #interaction of two arrays와 같은 원리로 비교해서 dp에 결과값 담기
        for i in e_order:
            r = len(start)
            # print(i, end[i], l,r)

            if i > s_order[-1]: #end값이 start의 모든 값 보다 큰 경우 비교할 필요 없음
                out = -1
            else:
                while l < r:
                    mid = (l + r) // 2
                    out = start[s_order[mid]] #rdp에 담아질 값
                    # print(s_order,mid, l, r,out)
                    if s_order[mid] == i: #같은 값이 걸린 경우 빠져나오기
                        l = mid
                        break

                    elif l != mid:
                        if s_order[mid] < i: #end값보다 start 값이 큰 경우
                            l = mid
                        else: #end값 보다 start값이 작은 경우
                            r = mid
                    else: #a마지막까지 와서 같은 값이 안나오는 경우
                        if s_order[mid] < i:
                            out = start[s_order[mid + 1]]
                        break

            for x in end[i]:
                dp[x] = out

        return dp
