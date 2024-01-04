'''
the train always departures from station 1, this is true for every day
so no need to worry about when we can get on the train
this should be very easy
'''


import sys
# sys.setrecursionlimit(99999) # because who gives a

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

'''
the subway route
'''
subway_route = list(map(int, input().split())) # [time] = stationID
time_subway_arrive = [0 for _ in range(n+1)] #[station] = time

for i in range(len(subway_route)):
    time_subway_arrive[subway_route[i]] = i


# we call the station where we transfer from subway to walways "station_transfer"
station_transfer_in_increasing_time_order = [] # in increasing order of time needed to arrival
time_needed_to_arrive_through_station_transfer = {}
for station_transfer in range(1, n+1):
    if station_to_destination_time_walkways[station_transfer] != float("inf"):
        time_needed_to_arrive_through_station_transfer[station_transfer] = time_subway_arrive[station_transfer] + station_to_destination_time_walkways[station_transfer]
        station_transfer_in_increasing_time_order.append(station_transfer)

def merge(indexes1, indexes2, values):
    indexes_sorted = []
    while (len(indexes1) and len(indexes2)):
        if values[indexes1[0]] < values[indexes2[0]]:
            indexes_sorted.append(indexes1.pop(0))
        else:
            indexes_sorted.append(indexes2.pop(0))
    # at this point, one of the two lists are empty
    indexes_sorted = indexes_sorted + indexes1 + indexes2
    return indexes_sorted


def mergesort(indexs, values:dict):
    if len(indexs) == 1:
        return indexs
    
    left = mergesort(indexs[0:len(indexs)//2], values)
    right = mergesort(indexs[len(indexs)//2: len(indexs)], values)

    return merge(left, right, values)

station_transfer_in_increasing_time_order = mergesort(station_transfer_in_increasing_time_order, time_needed_to_arrive_through_station_transfer)
station_index_in_STIITO = dict()
for i in range(len(station_transfer_in_increasing_time_order)):
    station_index_in_STIITO[station_transfer_in_increasing_time_order[i]] = i


def b_search_index(value, indexes_sorted:list, values:dict, left_bound=0, rightbound=-1):
    if rightbound == -1:
        rightbound = len(indexes_sorted)

    if (rightbound - left_bound == 2):
        return left_bound + 1
    if (rightbound - left_bound == 1):
        if value < values[indexes_sorted[left_bound]]:
            return left_bound-1
        return left_bound + 1
    
    mid = (left_bound + rightbound) // 2
    if value < values[indexes_sorted[mid]]:
        return b_search_index(value, indexes_sorted, values, left_bound=left_bound, rightbound=mid)
    return b_search_index(value, indexes_sorted, values, left_bound=mid, rightbound=rightbound)


def update_time_needed_arrive_through_transfer(station):
    if station not in station_transfer_in_increasing_time_order:
        return
    time_needed_to_arrive_through_station_transfer[station] = time_subway_arrive[station] + station_to_destination_time_walkways[station]
    station_transfer_in_increasing_time_order.pop(station_index_in_STIITO[station])
    newindex = b_search_index(time_needed_to_arrive_through_station_transfer[station], station_transfer_in_increasing_time_order, time_needed_to_arrive_through_station_transfer)
    station_transfer_in_increasing_time_order.insert(newindex, station)
    station_index_in_STIITO[station] = newindex

def swap_route(s1,s2):
    time_subway_arrive[subway_route[s1]] = s2 
    time_subway_arrive[subway_route[s2]] = s1
    swap = subway_route[s1]
    subway_route[s1] = subway_route[s2]
    subway_route[s2] = swap
    update_time_needed_arrive_through_transfer(subway_route[s1])
    update_time_needed_arrive_through_transfer(subway_route[s2])


''' 
for the n days
'''
for _ in range(d):
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)
    print(time_needed_to_arrive_through_station_transfer[station_transfer_in_increasing_time_order[0]])

# TODO WA