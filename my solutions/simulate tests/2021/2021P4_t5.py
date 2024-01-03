'''
Here is my understanding to this problem.

For each day, we define the following tables:
    1. Subway_route = [station1, station2, station3, ..., stationN] by order at which the train arrives.
    2. Time_subway_arrive[stationID] = the time at which the subway arrives at this station.
    
Now we can draw an important conclusion:
    If we can get (using walways) from start to any stationX in time t <= time_subway_arrive[stationX], we are definately able to get to any station after stationN in t=time_subway_arrive[stationID], including the end.

Based on the conclusion, there are four methods we can get to destination:
    1. start -> walways -> end
    2. start -> subway -> end
    3. start -> subway -> walways -> end
    4. start -> walways -> subway -> walways -> end
NOTE that any other moves that jumps between subway and walways, such as "start -> subway -> walways -> subway -> end" will be completely meaningless.
Because according to the conclusion, it will always take time_subway_arrive[stationID] much time to get to a station by subway.

So we can solve the problem by:
(Preparation)
    1. Using the dijkastra's algorithm, compute station_to_destination_time_walways[stationID] = the time needed to get from a station to stationN, using walkways only.
    2. Using the dijkastra's, compute start_to_station_walkways[stationID] = time needed to get from station0 to stationID, using walways only.
(Solution)
    3. For each day, compute subway_route and time_subway_arrive. 
        NOTE that we don't need to walk through all stations, just swap the two station.
    4. Create a variable called catch_subway_time for the minimum amount of time needed to get on the train.
        For any station i, if start_to_station_walkways[i] <= time_subway_arrive[i], catch_subway_time will be AT MOST time_subway_arrive[i] because we can catch the train at that station.
        NOTE that we don't need to look at all the stations, just look at the stations of which their subway arrival time are beeing swaped
    5. Now it will be very easy to compute the time needed to get from start to destination (we define as time_arrival), based on the travel method we use:
        (1: start -> walways -> end) time_arrival = start_to_station_walkways[0]
        (2: start -> subway -> end) time_arrival = time_subway_arrive[n]
        (3: start -> subway -> walways -> end) or (4: start -> walways -> subway -> walways -> end), we let stationT be the station at which you transfer from subway to walways
            time_arrival = time_subway_arrive[stationT] + station_to_destination_time_walways[stationT]
'''


import sys
# sys.setrecursionlimit(99999) # because who gives a

n, w, d = map(int, input().split())

walways = {}  # stores the walways, walways[stationX] = [station1, station2, ...], stations that stationX connects to
walways_reversed = {} # stores the walways, but reversed, walways_reversed[stationX] = [station1, station2, ...], stations that connects to stationX
for i in range(w): # input the walways
    start, end = map(int, input().split())
    # we change every point to 0~n-1
    start -= 1 # TODO this does not mtach
    end -= 1
    # add them to the table
    if start in walways:
       walways[start].append(end) 
    else:
       walways[start] = [end]
    if end in walways_reversed:
       walways_reversed[end].append(start)
    else:
       walways_reversed[end] = [start]



# run the dijkastra's to find the time needed to get from a station to stationN, using walkways only

station_to_destination_time_walkways = dict()
for i in range(n-1):
   station_to_destination_time_walkways[i] = float("inf")
station_to_destination_time_walkways[n-1] = 0
visited_stations = set([n-1]) # start from station n
flag = True
while flag:
    flag = False
    for walkway_end in visited_stations:
        if walkway_end not in walways_reversed:
            continue
        for walkway_start in walways_reversed[walkway_end]:
            if station_to_destination_time_walkways[walkway_start] > station_to_destination_time_walkways[walkway_end]+1:
                station_to_destination_time_walkways[walkway_start] = station_to_destination_time_walkways[walkway_end]+1
                flag = True 
                break
        if flag:
            break
    if flag:
        visited_stations.add(walkway_start)

start_to_station_walkway = dict()
for i in range(1, n):
   start_to_station_walkway[i] = float("inf")
start_to_station_walkway[0] = 0
visited_stations = set([0]) # start from station 0
flag = True
while flag:
    flag = False
    for walkway_start in visited_stations:
        if walkway_start not in walways:
            continue
        for walkway_end in walways[walkway_start]:
            if start_to_station_walkway[walkway_end] > start_to_station_walkway[walkway_start]+1:
                start_to_station_walkway[walkway_end] = start_to_station_walkway[walkway_start]+1
                flag = True 
                break
        if flag:
            break
    if flag:
        visited_stations.add(walkway_end)


'''
the subway route
'''
subway_route = list(map(int, input().split())) # [time] = stationID
time_subway_arrive = [0 for _ in range(n+1)] #[station] = time
catch_train_time = float("inf") # the min time we need to be on the train
catch_train_station = None

for i in range(len(subway_route)):
    time_subway_arrive[subway_route[i]] = i

def update_catch_train_time():
    global catch_train_time, catch_train_station
    for i in range(len(subway_route)):
        print(subway_route[i])
        if i >= start_to_station_walkway[subway_route[i]]:
            if catch_train_time > i:
                catch_train_time = i
                catch_train_station = subway_route[i]

update_catch_train_time()

def swap_route(s1,s2):
    swap = subway_route[s1]
    subway_route[s1] = subway_route[s2]
    subway_route[s2] = swap
    time_subway_arrive[subway_route[s1]] = s2 
    time_subway_arrive[subway_route[s2]] = s1

    if s1 == catch_train_station or s2 == catch_train_station:
        update_catch_train_time() # only updat when the station in which we catch our train changes


''' 
for the n days
'''
for _ in range(d):
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)

    shortest_path_time = station_to_destination_time_walkways[0]
    for time in range(catch_train_time+1, n): 
        # TODO we don't need to look for all the stations, pick the stations that are able to reach the destination with walways when update_catch_train_time, and examine them only
        current_station = subway_route[time]
        if station_to_destination_time_walkways[current_station] != float("inf"):
            shortest_path_time = min(station_to_destination_time_walkways[current_station] + time)

    print(shortest_path_time)