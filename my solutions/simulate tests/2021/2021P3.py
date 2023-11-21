n = int(input())

friends = []
'''
思路，定义对于朋友i，我在c出所需多花费的时间为fi(c)
这个函数会由三段折线构成，中间的
'''
class Line:
    starting_point=(0,0) # c, time
    ending_point=(0,0)
    minimum = 0
    k = 0
    b = 0
    def k_b_to_line(k, b, starting_x, ending_x):
        return Line((starting_x, k*starting_x+b), (ending_x, k*ending_x+b))
    def __init__(self, starting_point, ending_point):
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.minimum = min(starting_point[1], ending_point[1])
        self.k = (ending_point[1] - starting_point[1]) / (ending_point[0] - starting_point[0])
        self.b = starting_point[1] - starting_point[0] * k 
    
    def seperate(self, x):
        return [Line(self.starting_point, (x, k*x+b)), Line((x, k*x+b), self.ending_point)]

class LineSegments:
    self.lines = []
    pts_sep = []
    def __init__(self, initial_lines):
        self.lines = initial_lines
        for i in initial_lines:
            pts_sep.append(i.ending_point[0])
        pts_sep.pop(-1)
    def b_search(l, x, mi, ma):
        if len(l) < 3:
            for i in range(mi, ma):
                if l[i] == x:
                    return i
        guess = int((ma-mi)/2)
        if l[guess]  < x:
    def get_pos(self, pt):
        
    def addLines(self, lines):
        
for i in range(n):
    friends.append(