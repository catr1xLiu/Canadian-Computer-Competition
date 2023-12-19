n, w, d = map(int, input().split())

connections = {}
for i in range(w):
    a, b = map(int, input().split())
    start = min(a,b)-1
    end = max(a,b)-1
    try:
        connections[end].append(start)  # we change every point to 0~n-1
    except KeyError:
        connections[end] = [start]

time_arrival = [([float("inf")] * n) for i in range(n)] # [station][time] = time_arrival

for train_pos in range(n):
    time_arrival[train_pos][train_pos] = n



# mark the time needed to arrive for each station at earch time and change the markings every day