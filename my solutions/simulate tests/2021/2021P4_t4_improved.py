n, w, d = map(int, input().split())


'''
4 3 3
1 2
3 4
4 1
1 4 3 2
3 4
4 2
3 2
'''
connections = {}
for i in range(w):
    start, end = map(int, input().split())
    try:
        connections[start].append(end)  # we change every point to 0~n-1
    except KeyError:
        connections[start] = [end]

time_arrival_results = {} # [station][time] = time_arrival

subway_route = list(map(int, input().split())) # [time] = stationID


def reset_results():
    global time_arrival_results
    time_arrival_results = {}
    for i in range(1, n+1):
        time_arrival_results[i] = [-1] * n

def swap_route(s1,s2):
    swap = subway_route[s1]
    subway_route[s1] = subway_route[s2]
    subway_route[s2] = swap

time_needed_to_get_to_pos = [0 for i in range()] # TODO [start][end] = time_needed
def find_all_paths_from_point(pos, time=0):
    # TODO work on this, find and sort all possible paths, which are combination of 
    if pos in paths or (pos not in connections):
        return
    for end in range(connections[pos]):
        paths[end]

def time_arrival(pos, time):
    if time > n-1:
        return float("inf")
    if time_arrival_results[pos][time] != -1:
        return time_arrival_results[pos][time]
    if pos == n:
        return time 
    res = float("inf")
    if subway_route[time] == pos and time+1 < len(subway_route):
        res = min(res, time_arrival(subway_route[time+1], time+1))
    if pos in connections:
        for end in connections[pos]:
            res = min(res, time_arrival(end, time+1))
    time_arrival_results[pos][time] = res
    return res

for day in range(d):
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)
    reset_results()
    print(time_arrival(1,0))
