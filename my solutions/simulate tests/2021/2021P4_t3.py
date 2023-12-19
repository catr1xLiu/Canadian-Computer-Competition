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
    a, b = map(int, input().split())
    start = min(a,b)-1
    end = max(a,b)-1
    try:
        connections[start].append(end)  # we change every point to 0~n-1
    except KeyError:
        connections[start] = [end]

time_arrival_results = []

route = list(map(int, input().split())) # here the stations are 1~n, not 0~n-1
route_sorted = dict() # [start] = (time, end)

def sort_stations():
    global route_sorted
    route_sorted = dict()
    for i in range(len(route)-1):
        start = route[i]-1
        time = i
        end = route[i+1]-1
        route_sorted[start] = (time, end)

def reset_results():
    global time_arrival_results
    time_arrival_results = [[-1] * n for i in range(n)]

def time_arrival(pos, time):
    if time_arrival_results[pos][time] != -1:
        return time_arrival_results[pos][time]
    if pos == n:
        return time
    if route_sorted[pos][0] == time:
        res = time_arrival(route_sorted[pos][1], time+1)
        time_arrival_results[pos][time] = res 
        return res 
    for end in connections[pos]:
        res = time_arrival(end, time+1)
        time_arrival_results[pos][time] = res 
        return res 
    time_arrival_results[pos][time] = float("inf")
    return float("inf")


def swap_route(x, y):
    swap = route[x]
    route[x] = route[y]
    route[y] = swap 

for i in range(d):
    x, y = map(int, input().split())
    swap_route(x-1,y-1)
    sort_stations()
    reset_results()
    print(time_arrival(0,0))