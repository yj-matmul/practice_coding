#변수 받기
r, c, k = map(int, input().split())
arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

#count해서 새 array로 만들어주는 함수
def count_arr(arr):
    maxlen = 0
    newarr = []
    for row in range(len(arr)): #딕셔너리 형태로 세기
        nums = {}
        for j in arr[row]:
            if j == 0:
                pass
            elif j in nums:
                nums[j] += 1
            else:
                nums[j] = 1

        maxlen = max(maxlen, len(nums.keys())) #최대 길이
        lists = sorted(nums.items(), key=lambda x: x[0]) #숫자 기준 정렬, 딕셔너리를 튜플로
        lists = sorted(lists, key=lambda x: x[1]) #갯수 기준 정렬
        temp = []
        list(map(lambda x: temp.extend(list(x)), lists)) #정렬한 튜플형 리스트를 그냥 리르트로 변환
        newarr.append(temp) #리스트를 array에 담기

    return newarr, maxlen #새로만든 array, 최대 길이 리턴


def make_arr(arr, lens): #남은 자리에 0 채워주고 앞에 100개까지만 잘라주는 함수
    for i in range(len(arr)):
        if len(arr[i]) < lens * 2:
            arr[i].extend([0] * (lens * 2 - len(arr[i])))
        arr[i] = arr[i][:99]
    return arr


def transpose(arr): #트랜스포즈하는 함수
    temp = []
    for c in range(len(arr[0])):
        new_row = []
        for r in range(len(arr)):
            new_row.append(arr[r][c])

        temp.append(new_row)
    return temp


time = -1
out = 0

while time <= 100:
    time += 1
    if len(arr) >= r and len(arr[0]) >= c and arr[r - 1][c - 1] == k: #조건에 맞는 수가 올 경우 빠져나가기
        out = 1
        break
    else: #array 정렬
        if len(arr) >= len(arr[0]):
            newa, lens = count_arr(arr)
            newa = make_arr(newa, lens)
            arr = newa
        else:
            arr = transpose(arr)
            newa, lens = count_arr(arr)
            newa = make_arr(newa, lens)
            arr = transpose(newa)

if out == 1: #조건 맞춰서 빠져나왔는지 검사
    print(time)
else:
    print(-1)
