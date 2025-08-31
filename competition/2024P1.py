n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

ans = 0
for i in range(int(n/2)):
    if nums[i] == nums[i+int(n/2)]:
        ans+=1

print(ans*2)