''' second attempt of senior 2023 problem 4

Problem S4: Minimum Cost Roads

Problem Description

As the newly elected mayor of Kitchener, Alanna’s first job is to improve the city’s road
plan.
Kitchener’s current road plan can be represented as a collection of N intersections with M
roads, where the i-th road has length li meters, costs ci dollars per year to maintain, and
connects intersections ui and vi
. To create a plan, Alanna must select some subset of the
M roads to keep and maintain, and that plan’s cost is the sum of maintenance costs of all
roads in that subset.
To lower the city’s annual spending, Alanna would like to minimize the plan’s cost. However,
the city also requires that she minimizes travel distances between intersections and will reject
any plan that does not conform to those rules. Formally, for any pair of intersections (i, j),
if there exists a path from i to j taking l meters on the existing road plan, Alanna’s plan
must also include a path between those intersections that is at most l meters.
Input Specification
The first line contains the integers N and M.
Each of the next M lines contains the integers ui, vi, li
, and ci
, meaning that there currently
exists a road from intersection ui to intersection vi with length li and cost ci (1 ≤ ui
, vi ≤
N, ui
6 =
vi).
The following table shows how the available 15 marks are distributed.
Marks
Bounds on
Bounds on li
Bounds on ci
Additional
N and M
Constraints
3 marks
1 ≤ N, M ≤ 2 000
li = 0
1 ≤ ci ≤ 109
None
6 marks
1 ≤ N, M ≤ 2 000
1 ≤ li ≤ 109
1 ≤ ci ≤ 109
There is at most one road
between any unordered
pair of intersections.
6 marks
1 ≤ N, M ≤ 2 000
0 ≤ li ≤ 109
1 ≤ ci ≤ 109
None
Output Specification
Output one integer, the minimum possible cost of a road plan that meets the requirements.
Sample Input
5 7
1 2 15 1
2 4 9 9
5 2 5 6
4 5 4 4
4 3 3 7
1 3 2 7
1 4 2 1
Output for Sample Input
25
Explanation of Output for Sample Input
Here is a diagram of the intersections along with a valid road plan with minimum cost.
1
2
3
4
5
(15, 1)
(2, 7)
(2, 1)
(9, 9)
(5, 6)
(3, 7)
(4, 4)
Each edge is labeled with a pair (l, c) denoting that it has length l meters and cost c dollars.
Additionally, the roads that are part of the plan are highlighted in blue, with a total cost of
7 + 1 + 6 + 7 + 4 = 25.
It can be shown that we cannot create a cheaper plan that also respects the city’s requirements.
'''

'''
my solution 
if we are to find the minimum cost plan which satisfies all the traffic like before, we are actually removing all the roads that are redundant. since there is no additional cost for the travellers to take another road, we can simplify delete those roads that connects two points a and b but have a length greater than or eqial to the minimum distance to get from a to b using any other roads or the combination of several other roads
'''

from copy import deepcopy as cp

amount_of_intersects, amount_of_roads = map(int, input().split())

# input the roads
roads = dict() # {start:[road1 that starts from start, road2...], ...}
for i in range(amount_of_roads):
    road = tuple(map(int, input().split()))
    road2 = (road[1], road[0], road[2], road[3]) # reverse the Roads
    try:
        roads[road[0]].append(road)
    except KeyError:
        roads[road[0]] = [road] 
    try:
        roads[road2[0]].append(road2)
    except KeyError:
        roads[road2[0]] = [road2]    # append the roads to the dictionary by their starting points
        
# remove the repeated roads, or roads that start from and end in the same points
for start in roads:
    if len(roads[start]) == 0:
        continue
    for i in range(len(roads[start])-1):
        for j in range(i+1, len(roads[start])):
            if roads[start][i][1] != roads[start][j][1]: # if the two roads are differnt
                continue # just skip them
            # if the two roads are the same
            if roads[start][i][2] < roads[start][j][2]:
                roads.pop(j)
            elif roads[start][i][2] > roads[start][j][2]:
                roads.pop(i)   # choose the shorter road
            else: # if they cost the same
                if roads[start][i][3] > roads[start][j][3]:
                    roads.pop(i)
                    continue
                roads.pop(j)  #choose the cheaper road
                    
# find the minimum distance between every two points
found = dict() # {(from, to):min_distance, ...}

def dp(start, end, been_to = [], roads_taken=0):
    '''
    find the minimum distance between two points, if unreachable, return infinity
    Args:
    start(int): the starting point
    end(int): the desired desteny
    beend_to(list[int]): the points that we have already been to, to avoid dead loop
    roads_taken: the amount of roads that we have already taken
    
    Returns:
    (tuple) ((int)min_distance, (int)roads_taken): the distance of the minimum distance path, and the amount of roads in the found path
    '''
    if start == end: # if are already at the desteny
        return (0, roads_taken)
    try:
        return found[(start, end)] # if the path is already found, use the found result
    except KeyError:
        pass
    
    # find the shortest path
    been_to = cp(been_to)
    been_to.append(start)
    roads_taken_tmp = 0
    min_distance = float("inf")
    for road in roads[start]:   # try all the roads that starts from this point
        if road[1] in been_to: # if we have already been to the end of this road, do not take it as this will result in a dead loop
            continue
        distance = road[2] + dp(road[1], end, been_to, roads_taken+1)[0]  # the distance of the path from taking this road is the length of this road plus the minimum distance from the end of the road
        if distance < min_distance or (distance == min_distance and dp(road[1], end, been_to)[1] == 1):
            min_distance = distance
            roads_taken_tmp = dp(road[1], end, been_to, roads_taken+1)[1]
    if len(been_to) == 0:
        found[(start, end)] = (min_distance, roads_taken_tmp)
    return (min_distance, roads_taken_tmp)

roads_list = []  
for i in roads:
    roads_list += roads[i]

cost= 0
for i in range(len(roads_list)-1, -1, -1):
    road = roads_list[i]
    if road[2] > dp(road[0],road[1])[0]:
        continue
    if dp(road[0],road[1])[1] != 1:
        continue
    if road[1] > road[0]:
        cost += road[3]

print(cost)