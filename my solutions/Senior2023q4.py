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
        self.end = road.end
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
'''amount_of_intersects, amount_of_roads = map(int, input().split())
roads = [[] for i in range(amount_of_intersects)]  # the existing roads, the indexes are sorted by the starting point of each road and stored in the form of (ending, cost, length)
for i in range(amount_of_roads):
    u, v, cost, length = map(int, input().split())
    road = Road(u, v, cost, length)
    roads[road.start].append(road)'''
    
amount_of_intersects, amount_of_roads = 5,7
roads = [
    [Road(0, 1, 15, 1), Road(0, 2, 2, 7), Road(0, 3, 2, 1)],
    [Road(1, 3, 9, 9)],
    [],
    [Road(3, 4, 4, 4), Road(3, 2, 3, 7)],
    [Road(4, 1, 5, 6)]
]

answers = {}  # store the found answers to the minimum distance plans to go from one intersection to another,
# in the form of {(start, end):[plan1, plan2, plan3]

''' find all possible plans that have minimum distance in order to connect point "start" and "end" '''
def minimum_distance_plans(start:int, end:int) -> list:
    global answers

    # use found answers
    try:
        return answers[(start, end)]
    except KeyError:
        pass
    print(start, end)
    
    # if we reached the desteny
    if end == start:
        return [Plan(end)] # an empty plan with no roads
    
    # if we went over
    if start > end:
        return [] # all roads are stored in the way such that intersection points with smaller id are stored as starting points, making no backward movements are possible, so no plans will work

    for road in roads[start]: # go through all the roads that connect the current intersection and farther points
        current_plan = Plan(start)
        current_plan.connectRoad(road)
        min_distance = float("inf")
        
        plans_from_road_ending = minimum_distance_plans(road.end, end)
        min_distance_options = []
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

print(minimum_distance_plans(0,4)[0])
print(answers)
# according to all the choices that can achieve minimum distance, find the combination if choices where the cost is lowest
