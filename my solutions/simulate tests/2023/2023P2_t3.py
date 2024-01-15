n = int(input())
mounts = list(map(int, input().split()))

ans = [float("inf") for _ in range(n)]

for mid in range(n):
    # odd number length
    asym = 0
    left = mid-1
    right = mid+1
    while left >= 0 and right < n:
        asym += abs(mounts[right] - mounts[left])
        length = right-left
        ans[length] = min(ans[length], asym)
        left -= 1
        right += 1

    # even number length, the middle line is the space AFTER mid
    asym = 0
    left = mid
    right = mid+1
    while left >= 0 and right < n:
        asym += abs(mounts[right] - mounts[left])
        length = right-left
        ans[length] = min(ans[length], asym)
        left -= 1
        right += 1

ans[0] = 0

for i in ans:
    print(i, end=" ")

print()