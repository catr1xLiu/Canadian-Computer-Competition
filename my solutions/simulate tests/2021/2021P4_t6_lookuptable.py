'''
the train always departures from station 1, this is true for every day
so no need to worry about when we can get on the train
this should be very easy
'''

from time import perf_counter as us

n, w, d = map(int, input().split())

walways = {}  # stores the walways, walways[stationX] = [station1, station2, ...], stations that stationX connects to
walways_reversed = {} # stores the walways, but reversed, walways_reversed[stationX] = [station1, station2, ...], stations that connects to stationX
for i in range(w): # input the walways
    start, end = map(int, input().split())
    # we change every point to 0~n-1
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
for i in range(1, n+1):
   station_to_destination_time_walkways[i] = float("inf")
station_to_destination_time_walkways[n] = 0
visited_stations = set([n]) # start from station n
flag = True
while flag:
    nodes_to_be_added = []
    for walkway_end in visited_stations:
        if walkway_end not in walways_reversed:
            continue
        for walkway_start in walways_reversed[walkway_end]:
            if station_to_destination_time_walkways[walkway_start] > station_to_destination_time_walkways[walkway_end]+1:
                station_to_destination_time_walkways[walkway_start] = station_to_destination_time_walkways[walkway_end]+1
                nodes_to_be_added.append(walkway_start)
    if nodes_to_be_added:
        for i in nodes_to_be_added:
            visited_stations.add(i)
    else:
        break
'''
the subway route
'''
subway_route = list(map(int, input().split())) # [time] = stationID
time_subway_arrive = [0 for _ in range(n+1)] #[station] = time

for i in range(len(subway_route)):
    time_subway_arrive[subway_route[i]] = i


# we call the station where we transfer from subway to walways "station_transfer"
time_needed_to_arrive_through_station_transfer = {}
time_arrival_possible_results = [] # all the possible time_arrival 
time_arrival_results_count = dict() # [time_arrival] = amount of stations
for station_transfer in range(1, n+1):
    time_arrival_result = time_subway_arrive[station_transfer] + station_to_destination_time_walkways[station_transfer]
    time_needed_to_arrive_through_station_transfer[station_transfer] = time_arrival_result
    
    t0 = us()
    if time_arrival_result not in time_arrival_possible_results:
        time_arrival_possible_results.append(time_arrival_result)
        time_arrival_results_count[time_arrival_result] = 0
    print((us()-t0) * 1000)
    time_arrival_results_count[time_arrival_result] += 1
    print(station_transfer / n * 100, "%")
time_arrival_possible_results.sort()

def b_search_index(value, list_sorted:list, left_bound=0, rightbound=-1):
    if rightbound == -1:
        rightbound = len(list_sorted)

    if (rightbound - left_bound == 0):
        return 0
    if (rightbound - left_bound == 1):
        if value < list_sorted[left_bound]:
            return left_bound
        return left_bound + 1
    
    mid = (left_bound + rightbound) // 2
    if value < list_sorted[mid]:
        return b_search_index(value, list_sorted, left_bound=left_bound, rightbound=mid)
    return b_search_index(value, list_sorted, left_bound=mid, rightbound=rightbound)

def update_time_needed_arrive_through_transfer(station):
    time_arrival_result = time_subway_arrive[station] + station_to_destination_time_walkways[station]
    if time_arrival_result not in time_arrival_possible_results:
        time_arrival_possible_results.insert(b_search_index(time_arrival_result, time_arrival_possible_results), time_arrival_result)
        time_arrival_results_count[time_arrival_result] = 0
    time_arrival_results_count[time_arrival_result] += 1
    
    time_arrival_results_count[time_needed_to_arrive_through_station_transfer[station]] -= 1
    time_needed_to_arrive_through_station_transfer[station] = time_arrival_result


def swap_route(s1,s2):
    time_subway_arrive[subway_route[s1]] = s2 
    time_subway_arrive[subway_route[s2]] = s1
    swap = subway_route[s1]
    subway_route[s1] = subway_route[s2]
    subway_route[s2] = swap

    update_time_needed_arrive_through_transfer(subway_route[s1])
    update_time_needed_arrive_through_transfer(subway_route[s2])

def get_min_time():
    for result in time_arrival_possible_results:
        if time_arrival_results_count[result]:
            return result
    return float("inf")

''' 
for the n days
'''
for _ in range(d):
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)
    print(get_min_time())