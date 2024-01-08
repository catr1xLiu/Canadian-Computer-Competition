'''
the train always departures from station 1, this is true for every day
so no need to worry about when we can get on the train
this should be very easy
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self, step=0) -> str:
        string = f"node with value:{self.value}"
        if self.left is not None:
            string += f", left-brench:{self.left.__str__(step+1)}"
        if self.right is not None:
            string += f", right-brench:{self.right.__str__(step+1)}"
        return "\n" + "   "*step + "{\n}" + "   "*step + string + "\n" +  "   "*step + "}\n"
    
def create_btree(list_sorted):
    if len(list_sorted) == 1:
        return Node(list_sorted[0])
    if len(list_sorted) == 2:
        return Node(list_sorted[0], None, Node(list_sorted[1]))
    mid = (len(list_sorted)) // 2

    return Node(list_sorted[mid], create_btree(list_sorted[:mid]), create_btree(list_sorted[mid+1:]))

def add_node(tree:Node, newNode:Node, values_map):
    if values_map[newNode.value] > values_map[tree.value]:
        if tree.right is None:
            tree.right = newNode
        else:
            add_node(tree.right, newNode, values_map)
    elif values_map[newNode.value] < values_map[tree.value]:
        if tree.left is None:
            tree.left = newNode
        else:
            add_node(tree.left, newNode, values_map)

def find_path(tree:Node, value, values_map, path=[]):
    '''
    get the path, in a list
    0 means left, 1 means right
    -1 for unfound
    '''
    if value > values_map[tree.value]:
        if tree.right is None:
            return -1
        return find_path(tree.right, value, values_map, path=path + [1])
    if value < values_map[tree.value]:
        if tree.left is None:
            return -1
        return find_path(tree.left, value, values_map, path=path+[0])
    if tree.value == value:
        return path

def delete_node(tree:Node, path)->Node:
    # None if path invalid
    if path == -1 or len(path)==0:
        return None
    if len(path) == 1:
        if path[0]:
            swap = tree.right
            tree.right = None
            return swap
        swap = tree.left
        tree.left = None
        return swap
    
    if path[0]:
        return delete_node(tree.right, path[1:])
    return delete_node(tree.left, path[1:])

def leftMostNode(tree:Node):
    if tree.left is None:
        return tree.value
    return leftMostNode(tree.left)




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
station_transfer_btree = create_btree(station_transfer_in_increasing_time_order)


def update_time_needed_arrive_through_transfer(station):
    if station not in station_transfer_in_increasing_time_order:
        return
    time_needed_to_arrive_through_station_transfer[station] = time_subway_arrive[station] + station_to_destination_time_walkways[station]
    newNode = delete_node(station_transfer_btree, find_path(station_transfer_btree, time_needed_to_arrive_through_station_transfer[station], time_needed_to_arrive_through_station_transfer))
    add_node(station_transfer_btree, newNode, time_needed_to_arrive_through_station_transfer)


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
    # print("station in inc:", station_transfer_in_increasing_time_order)
    s1, s2 = map(int, input().split())
    swap_route(s1-1, s2-1)
    print(leftMostNode(station_transfer_btree))