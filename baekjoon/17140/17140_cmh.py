r, c, k = map(int, input().split())
A = []

for r in range(3):
    A.append(list(map(int, input().split())))


# R 연산
temp_A = []

for r in range(len(A)):
    dict = {}
    for c in range(len(A[r])):
        if A[r][c] not in dict.keys():
            dict[A[r][c]] = 1
        else:
            dict[A[r][c]] += 1

    print(dict)
    print(sorted(dict.items(), key = (lambda x:x[1]), reverse = True))

