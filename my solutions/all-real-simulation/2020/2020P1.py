n = int(input())

positions = {}
times = []

for i in range(n):
    t, p = map(int, input().split())
    times.append(t)
    positions[t] = p

times.sort()

max_vel = 0
for i in range(n):
    max_vel = max(abs(positions[times[i]]-positions[times[i-1]]) / (times[i]-times[i-1]), max_vel)

print(max_vel)