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


class Road:
    def __init__(self, start, end, length, cost):
        self.start = min(start, end)
        self.end = max(start, end)  # always take the intersection with smaller id as the starting point
        self.cost = cost
        self.length = length

    def __str__(self):
        return "road, from" + str(start) + "to" + str(end) + ", distance:" + str(length) + ", cost:" + str(cost)




# solution for 2023 question 4
amount_of_intersects, amount_of_roads = map(int, input().split())
roads = [[] for i in range(
    amount_of_intersects)]  # the existing roads, the indexes are sorted by the starting point of each road and stored in the form of (ending, cost, length)
for i in range(amount_of_roads):
    u, v, cost, length = map(int, input().split())
    start = min(u, v)  # always consider the smaller intersection as it's starting point
    end = max(u, v)
    road = (end, cost, length)
    roads[start].append(road)

answers = {}  # store the found answers to the minimum distance plans to go from one intersection to another,
# in the form of {(start, end):[plan1, plan2, plan3]
# each plan is defined as ([road1, road2, ....], distance)

'''  '''
