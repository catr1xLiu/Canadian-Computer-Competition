import sys
sys.setrecursionlimit(4000)

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

subway_route = list(map(int, input().split())) # [time] = stationID
time_subway_arrive = [0 for _ in range(n+1)] #[station] = time

for i in range(len(subway_route)):
    time_subway_arrive[subway_route[i]] = i


def reset_results():
    global time_arrival_results
    time_arrival_results = {}
    for i in range(1, n+1):
        time_arrival_results[i] = [-1] * n

def swap_route(s1,s2):
    swap = subway_route[s1]
    subway_route[s1] = subway_route[s2]
    subway_route[s2] = swap
    time_subway_arrive[subway_route[s1]] = s2 
    time_subway_arrive[subway_route[s2]] = s1


def time_arrival(pos, time, stations_been_to=[]):
    if time > n-1:
        return float("inf")
    if pos == n:
        return time 
    if time_arrival_results[pos][time] != -1:
        return time_arrival_results[pos][time]
    res = float("inf")
    if subway_route[time] == pos and time+1 < len(subway_route):
        res = min(res, time_arrival(subway_route[time+1], time+1, stations_been_to + [pos]))
    elif time_subway_arrive[pos] > time:
        res = min(res, time_arrival(pos, time_subway_arrive[pos], stations_been_to)) # wait for train
    if pos in connections:
        for end in connections[pos]:
            if end in stations_been_to:
                continue
            res = min(res, time_arrival(end, time+1, stations_been_to + [pos]))
    time_arrival_results[pos][time] = res
    return res

for day in range(d):
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)
    reset_results()
    print(time_arrival(1,0))


'''
we have been thinking too complicated in this problem
the things we have to take advantage are:
1. if you get on a subway, you manage to go to any point at the time they have the subway (ts)
2. there is no point getting off and then getting on a subway, as it is always going to take ts to get to a station by subway
3. running a dijkastra algorithm will be good

'''