'''
Problem S4: Good Triplets
Problem Description
Andrew is a very curious student who drew a circle with the center at (0, 0) and an integer
circumference of C ≥ 3. The location of a point on the circle is the counter-clockwise arc
length from the right-most point of the circle.
(0, 0)
C − 2
C − 1
0
1
2
Andrew drew N ≥ 3 points at integer locations. In particular, the i
th point is drawn at
location Pi (0 ≤ Pi ≤ C − 1). It is possible for Andrew to draw multiple points at the same
location.
A good triplet is defined as a triplet (a, b, c) that satisfies the following conditions:
• 1 ≤ a < b < c ≤ N.
• The origin (0, 0) lies strictly inside the triangle with vertices at Pa, Pb, and Pc. In
particular, the origin is not on the triangle’s perimeter.
Lastly, two triplets (a, b, c) and (a0 , b0 , c0 ) are distinct if a
6 =
a0 , b
6 =
b0 , or c
6 =
c0 .
Andrew, being a curious student, wants to know the number of distinct good triplets. Please
help him determine this number.
Input Specification
The first line contains the integers N and C, separated by one space.
The second line contains N space-separated integers. The i
th integer is Pi (0 ≤ Pi ≤ C − 1).

Output Specification
Output the number of distinct good triplets.
Sample Input
8 10
0 2 5 5 6 9 0 0
Output for Sample Input
6
Explanation of Output for Sample Input
Andrew drew the following diagram.
(0, 0)
P1, P7, P8
P2
P3, P4
P5
P6
0
1
9
2
3
4
5
6
7
8
The origin lies strictly inside the triangle with vertices P1, P2, and P5, so (1, 2, 5) is a good
triplet. The other five good triplets are (2, 3, 6), (2, 4, 6), (2, 5, 6), (2, 5, 7), and (2, 5, 8).
'''

'''
n,c = map(int,input().split())

points = list(set(map(int, input().split())))
points.sort()


def opposing_point(point):
    return (point + c // 2) % c
    
def position_of(point):
    left = 0
    right = len(points)-1
    while True:
        mid = (left + right) // 2
        if point > points[mid]:
            left = mid
        elif point < points[mid]:
            right = mid
        else:
            return mid
            
good_triangles_count = 0
for p1 in range(n-2):
    current_included_points = 0
    last_check = -1
    for p2 in range(p1+1, min(opposing_point(p1),n-1)):
        print(p1, p2, opposing_point(p2)-1)
        p3_bound = opposing_point(p2)
        if c%2 == 0:
            p3_bound = opposing_point(p2)-1
        if last_check == -1 and p3_bound in points:
            
        if last_check < len(points) and ( (c%2 == 0 and opposing_point(p2)-1 == points[last_check]) or (c%2 != 0 and opposing_point(p2) == points[last_check]) ):
            last_check += 1
            current_included_points += 1
        good_triangles_count += current_included_points

print(good_triangles_count)

'''



# second attempt
'''
my solution:
if we take a point on the circle, draw a line that goes through the point and the center of the circle, we call the intersection of the line with the circle the "opposing point" of the circle(see pic1)
if point 1 sits in the middle of the opposing points of point 2 and 3, the triangle that 123 forms will include the origin, other wise, the triangle does not include the origin (see pic2)
we can use this to quickly determine how many triangles are there that includes the origin within it
'''
n,c = map(int,input().split())

points = list(map(int, input().split()))
circle = [0 for i in range(c)] # the amount of points in each place of the circle 
for i in points:
    circle[i] += 1

def opposing_point(point):
    return (point + c // 2) % c

# brut-force version
def includes(range_lower, range_upper, point):
    '''
    find whether the point is inside the range
    '''
    if range_upper-range_lower == c/2 == c//2:  # when the range is exactly half the circle
        return False # you can't really say is the point inside this rsnge, however the question says that the origin must be stricly included inside the triangle to make the triangle good, so let's go no, because two opposing points will make one of the side of the triangle going through the origin, and the triangle will be bad
    included = range_lower < point < range_upper # whether the point inside the range
    if range_upper - range_lower > c // 2:  # if the range is bigger than half the circumference, we need to think of the actual range as the opposite of the raw range
        return not included
    # other wise, just give the straight-up answer
    return included

good_triangles_count = 0
for p1 in range(c-2):
    for p2 in range(p1, c-1):
        for p3 in range(p2, c):
            lower_opposing_point = min(opposing_point(p1), opposing_point(p2))
            upper_opposing_point = max(opposing_point(p1), opposing_point(p2))
            good_triangles_count += int(includes(lower_opposing_point, upper_opposing_point, p3) * circle[p1] * circle[p2] * circle[p3])
print(good_triangles_count)

good_triangles_count = 0
if c%2 == 0: # if the circle has even number of points
    # go through all thebpossible triangles with p1<p2<p3
    for p1 in range(c//2 -1):  # the first point of the triangle cannot exceed the point before the second half of the circle(assuming that we devide it through its diameter from the point0). This is because p1<p2<p3, meaning that the other 
        if circle[p1] == 0:
           continue
        p1_scale = circle[p1] # if there are n points in the position p1, the amount of good triangles found using p1 will scale by n times
        current_included_points = 0
        for p2 in range(p1+2, min(opposing_point(p1),n-1)):
            p2_scale = circle[p2]
            print(p1, p2, opposing_point(p2)-1)
            p3_bound = opposing_point(p2)
            if c%2 == 0:
                p3_bound = opposing_point(p2)-1
            current_included_points += circle[p3_bound]
            good_triangles_count += current_included_points * p1_scale * p2_scale
else:
    
print(good_triangles_count)