'''
Problem S4: Minimum Cost Roads

Problem Description
As the newly elected mayor of Kitchener, Alanna’s first job is to improve the city’s road plan.
Kitchener’s current road plan can be represented as a collection of N intersections with M roads, where the i-th road has length li meters, costs ci dollars per year to maintain, and connects intersections ui and vi
To create a plan, Alanna must select some subset of the M roads to keep and maintain, and that plan’s cost is the sum of maintenance costs of all roads in that subset.
To lower the city’s annual spending, Alanna would like to minimize the plan’s cost. However,the city also requires that she minimizes travel distances between intersections and will reject any plan that does not conform to those rules. Formally, for any pair of intersections (i, j), if there exists a path from i to j taking l meters on the existing road plan, Alanna’s plan must also include a path between those intersections that is at most l meters.

Input Specification
The first line contains the integers N and M.
Each of the next M lines contains the integers ui, vi, li, and ci, meaning that there currently exists a road from intersection ui to intersection vi with length li and cost ci (1 ≤ ui, vi ≤N, ui != vi).

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
Here is a diagram of the intersections along with a valid road plan with minimum cost. [2023question4.jpg]
Each edge is labeled with a pair (l, c) denoting that it has length l meters and cost c dollars.
Additionally, the roads that are part of the plan are highlighted in blue, with a total cost of 7 + 1 + 6 + 7 + 4 = 25.
It can be shown that we cannot create a cheaper plan that also respects the city’s requirements.
'''

from copy import deepcopy as cp

class Road: # stores a single road
    def __init__(self, start, end, length, cost):
        self.start = min(start, end)
        self.end = max(start, end)  # always take the intersection with smaller id as the starting point
        self.cost = cost
        self.length = length

    def __str__(self):
        return "road, from" + str(self.start) + "to" + str(self.end) + ", distance:" + str(self.length) + ", cost:" + str(self.cost)


class Plan: # stores a path to get from one intersection to another
    def __init__(self, start):
        self.start = start
        self.end = start
        self.distance = 0
        self.cost = 0
        self.path = []

    def __str__(self):
        path_string = ""
        for road in self.path:
            path_string += str(road) + ','
        return "path that connects:" + str(self.start) + "and" + str(self.end) + ", with total distance:" + str(self.distance) + " and total cost:" + str(self.cost) + ". Connected roads:" + path_string

    def connectRoad(self, road:Road): # connect a road to the end of the path, and update all the datas
        if self.start == road.start:
            # if the road is connected normally
            self.end = road.end
        elif self.start == road.end: 
            # if the road is connected reversely
            self.end = road.start
        else:
            return
        self.distance += road.length
        self.cost += road.cost
        self.path.append(road)
    
    def connectPlan(self, plan): # to connect to another plan
        if self.end != plan.start:
            return
        self.path += plan.path
        self.cost += plan.cost
        self.distance += plan.distance
        self.end = plan.end
        
    def getCopy(self): # create a copy of current plan
        copy = Plan(self.start)
        for road in self.path:
            copy.connectRoad(road)
        return copy


# solution for 2023 question 4
amount_of_intersects, amount_of_roads = map(int, input().split())
roads = []  # the existing roads, the indexes are sorted by the starting point of each road and stored in the form of (ending, cost, length)
for i in range(amount_of_roads):
    u, v, cost, length = map(int, input().split())
    road = Road(u-1, v-1, cost, length)
    roads.append(road)
    

'''amount_of_intersects, amount_of_roads = 5,7
roads = [
    [Road(0, 1, 15, 1), Road(0, 2, 2, 7), Road(0, 3, 2, 1)],
    [Road(1, 3, 9, 9), Road(1, 4, 5, 6)],
    [Road(2, 3, 3, 7)],
    [Road(3, 4, 4, 4)],
    []
]'''

answers = {}  # store the found answers to the minimum distance plans to go from one intersection to another,
# in the form of {(start, end):[plan1, plan2, plan3]

''' find all possible plans that have minimum distance in order to connect point "start" and "end", we do not reuse any roads by skipping any roads in "used_roads" '''
def minimum_distance_plans(start:int, end:int, intersects_been_to:list = []) -> list:
    global answers

    # use found answers
    try:
        return answers[(start, end)]
    except KeyError:
        pass
    
    # if we reached the desteny
    if end == start:
        return [Plan(end)] # an empty plan with no roads

    min_distance = float("inf")
    min_distance_options = []
    for road in roads: # go through all the roads that connect the current intersection and farther points
        if road.start != start and road.end != start: # if the road is unrelated
            continue

        current_plan = Plan(start)
        current_plan.connectRoad(road)
        if current_plan.end in intersects_been_to:
            continue # never go through intersects that we've been to since that will lead to dead loops
        plans_from_road_ending = minimum_distance_plans(current_plan.end, end, cp(intersects_been_to) + [current_plan.end])
        
        for plan in plans_from_road_ending:
            combined_plan = current_plan.getCopy()
            combined_plan.connectPlan(plan)
            if combined_plan.distance < min_distance:
                min_distance = combined_plan.distance
                min_distance_options = []
            if combined_plan.distance == min_distance:
                min_distance_options.append(combined_plan)
    
    answers[(start, end)] = min_distance_options 
    return min_distance_options

# according to all the choices that can achieve minimum distance, find the combination if choices where the cost is lowest

'''
all the frontward connection between every two intersections:
[
    [plan1, plan2, plan3], # the plans to connect the first pair of intersections
    [plan1], # the plans to connect the second pair of intersections
    [plan1, plan2], # the plans to connect the third pair of intersections
]
'''
plans_for_all_connections = []
for start in range(amount_of_intersects-1):
    for end in range(start+1, amount_of_intersects):
        plans_for_all_connections.append(minimum_distance_plans(start, end))


def contains(roads:list, road:Road):
    for i in roads:
        if i.start == road.start and i.end == road.end and i.cost == road.cost and i.length == road.length:
            return True
    return False

def find_total_cost(plans: list) -> int: # find the total cost of a set of plans if they are aplied at the sametime, note that roads may repeat and they shouldn't be counted twice
    roads = []
    for plan in plans:
        for road in plan.path:
            if contains(roads, road):
                continue
            roads.append(road) # the road objects are all created during input, so they won't repreat in the set
    total_cost = 0
    for road in roads:
        total_cost  += road.cost
        print(road)
    print(total_cost, "\n\n\n\n")
    return total_cost

min_cost = float("inf")
def dfs(connection_count:int, choices:list):
    global min_cost
    if connection_count == len(plans_for_all_connections)-1:
        min_cost = min(min_cost, find_total_cost(choices))
        return
    for plan in plans_for_all_connections[connection_count]:
        dfs(connection_count+1, cp(choices) + [plan])


dfs(0, [])
print(min_cost)