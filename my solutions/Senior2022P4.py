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
Lastly, two triplets (a, b, c) and (a
0
, b0
, c0
) are distinct if a 6= a
0
, b 6= b
0
, or c 6= c
0
.
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
P5 P6
0
1
9
3 2
4
5
6
7 8
The origin lies strictly inside the triangle with vertices P1, P2, and P5, so (1, 2, 5) is a good
triplet. The other five good triplets are (2, 3, 6), (2, 4, 6), (2, 5, 6), (2, 5, 7), and (2, 5, 8).
'''

