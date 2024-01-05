'''
the dijkastra's algorithm

this algorithm is suitable for the kind of question that have the following characteristics:
1. nodes are connected with waited and directed walways
2. you are to find the shortest distance between one node to every other node

example: 
there are n nodes and w one-way walways connecting them
each walway takes you from S_i to E_i and has distance D_i, where S_i and Ei both <= n-1
you need to find out the shortest distance between x and all the other nodes
output the distances from node x to all the other nodes(from node 0 to node n-1) 
if a node is not reachable, output infinity
for node x, output 0
'''

# input the data
n, w = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(n)]
x = int(input())

# sort the data
roads_reaching_from_node = dict() #[nodeID] = [road1, road2, road3]
for road in roads:
    if road[0] not in roads_reaching_from_node:
        roads_reaching_from_node[road[0]] = []
    roads_reaching_from_node[road[0]].append(road)


distances_from_x = [float("inf") for _ in range(n)] # stores the distances from x
distances_from_x[x] = 0 # the distance from x to x is 0
# the roads that we have alrady visited, starting from x
visited = set()
visited.add(x)

while True: # updates the distances to nodes by taking the roads that lead to them, until no new update can come through
    nodes_visited_during_this_loop = [] # the roads that have been updated during this loop
    for road_start in visited:
        for road_reaching_from_start in roads_reaching_from_node[road_start]: # examine all the roads that reaches from a visited node to other nodes
            road_end = road_reaching_from_start[1] # where the road leads to
            road_distance = road_reaching_from_start[2] # the distance of the road
            if distances_from_x[road_end] > distances_from_x[road_start] + road_distance: # if taking this raod from road_start is a quicker way to reach road_end than mothods before
                distances_from_x[road_end] = distances_from_x[road_start] + road_distance # make it the shortest
                nodes_visited_during_this_loop.append(road_end)
    if nodes_visited_during_this_loop:
        for node in nodes_visited_during_this_loop:
            # add all the nodes that we have visited this round to the visited list
            visited.add(node)
    else:
        # if there are no updates to our graph, this would mark the end of our program
        break

print(distances_from_x)

'''
test data:
10 10
0 1 2
1 2 3
2 3 4
3 4 2
4 5 4
5 6 5
6 7 3
7 8 2
8 9 3
9 0 4
4
'''