peoples = int(input())
times = list(map(int, input().split()))

times.sort()
count = [0]
for i in range(peoples):
    count.append(count[i] + times[i])

print(sum(count))




peoples = int(input())
times = list(map(int, input().split()))

times.sort()
count = [0, 0]
for i in range(peoples):
    count[0] = count[0] + times[i]
    count[1] += count[0]

print(count[1])