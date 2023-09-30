n = int(input())
_ = input().split()
mounts = []
for i in _:
    mounts.append(int(i))

def mina(length):
    ans = float("inf")
    for bias in range(n - length+1):
        crop = mounts[bias:bias+length]
        ans = min(avalue(crop), ans)
    return ans

def avalue(crop):
    ans = 0
    for i in range(0, len(crop) // 2):
        left = crop[i]
        right = crop[-1-i]
        ans += abs(right-left)
        counts += 1
    return ans
        

for i in range(1,n+1):
   #print(mina(i), end=" ")
   mina(i)


print()

