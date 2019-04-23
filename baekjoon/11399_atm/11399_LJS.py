n = int(input())
nums = list(map(int, input().split()))

nums.sort()
dp = [0] * n
dp[0] = nums[0]
count = 1
for num in nums[1:]:
    dp[count] = dp[count-1] + num
    count+=1

print(sum(dp))