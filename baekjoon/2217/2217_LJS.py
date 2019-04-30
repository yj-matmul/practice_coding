n = int(input())
rope = []
while n:
    rope.append(int(input()))
    n-=1

rope.sort()
max_point = 0
for i in range(len(rope)):
    point = rope.pop() * (i+1)
    if point > max_point:
        max_point = point

print(max_point)