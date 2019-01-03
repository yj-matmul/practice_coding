nums = [1, 2, 3, 1]

answer = 0
x = 0

while(x < len(nums) - 2):
    if nums[x+2] >= nums[x] + nums[x+1]:
        answer += nums[x+2]
    else:
        answer += nums[x]
    x += 1

print(answer)
