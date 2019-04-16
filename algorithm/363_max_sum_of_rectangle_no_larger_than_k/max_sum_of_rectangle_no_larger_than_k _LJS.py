def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
    row, col = len(matrix), len(matrix[0])
    result = float('-inf')
    # kadane 알고리즘을 이차원 배열에서 사용한다.
    # 한 col을 기준으로 sums를 만들고, col의 인덱스를 한칸씩 옮기면서 sums의 각 항에 더해준다.
    # 그 sums를 maxSubArray 함수에 넣어서 max_sum을 뽑아서 최종 result와 비교
    for l in range(col):
        sums = [0] * row
        for r in range(l, col):
            for i in range(row):
                sums[i] += matrix[i][r]
            result = max(result, self.maxSubArray(sums, k))
    return result


def maxSubArray(self, nums, k):
    cur_sum, max_sum = 0, float('-inf')
    sums = [0]
    for i, n in enumerate(nums, 1):
        cur_sum += n
        idx = bisect.bisect_left(sums, cur_sum - k)
        # cur_sum 이 계산 안해도 될만큼 커짐(k를 넘긴 상태)면, idx가 sums의 마지막 인덱스를 가리키고, 그 경우 if문으로 들어가지 않는다.
        # 즉, sums[idx]가 index error를 일으키지 않음. 추가로 max 비교또한 하지 않음.
        if idx != i:
            max_sum = max(max_sum, cur_sum - sums[idx])
        bisect.insort(sums, cur_sum)
    return max_sum