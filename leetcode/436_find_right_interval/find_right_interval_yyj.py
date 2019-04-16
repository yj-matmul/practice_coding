# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals: List[Interval]) -> List[int]:
        st = []  # 정렬되지 않은 interval의 start 값들
        answers = []  # 최종 결과 (index 담을 공간)
        min_starts = []  # 각 interval의 end에서 오른쪽으로 가까운 start 값들

        for interval in intervals:
            st.append(interval.start)

        starts = sorted(st)  # 정렬된 start 값들 (for binary search)

        for interval in intervals:
            end = interval.end

            # 정렬된 start의 가장 큰 값보다 end가 큰 경우
            if end > starts[-1]:
                min_starts.append(-1)
                continue

            # binary search 적용
            low = 0
            high = len(starts)
            while low <= high:
                mid = (low + high) // 2
                if starts[mid] < end:
                    low = mid + 1
                elif starts[mid] > end:
                    high = mid - 1
                else:
                    break

            # 혹시 모를 오차를 위해
            if starts[mid] < end: mid += 1
            min_starts.append(starts[mid])

        # answers에 index를 담기 위한 과정
        for i in range(len(min_starts)):
            if min_starts[i] == -1:
                # 실제 interval의 start가 -1인 경우를 고려
                if (-1 in st) and (intervals[i].end <= -1):
                    answers.append(st.index(min_starts[i]))
                else:
                    answers.append(-1)
                continue
            answers.append(st.index(min_starts[i]))

        return answers
