'''
思路转变，算出总共有多少个Triplets不是好的，然后用总数减去它
第一个点为i的三角，有(c-i-1) + (c-i-2) + (c-i-3) + ... + 0 用等差数列就行
接下来，对于第一个点为Pi的三角形，第二个点位Pj的三角形

算法错力，bad points不一定必须全在p1所在直径的一侧才叫在一侧。任意直径的一侧都算
'''

n, c = map(int, input().split())
pts_at_loc = [0 for i in range(c)]

for pos in map(int, input().split()):
    pts_at_loc[pos] += 1

half_circ = int(c / 2) + c % 2  # half of the circle


def select2(n):
    # select 2 random pts from n points, orders don't matter
    return (n - 1) * n / 2  # (n-1) + (n-2) + ... + 1


total_trips = 0
for i in range(2, n):
    total_trips += select2(i)

for pts in pts_at_loc:
    if pts >= 3:
        for i in range(2, pts):
            total_trips -= select2(i)  # get rid of inner selection

good_trips = total_trips

upper_half_pts = sum(pts_at_loc[1:half_circ + 1])
lower_half_pts = sum(pts_at_loc[half_circ:c])
for p1_loc in range(c - 2):
    print(p1_loc, select2(upper_half_pts), select2(lower_half_pts))
    if upper_half_pts >= 0:
        good_trips -= select2(upper_half_pts) * pts_at_loc[p1_loc]
    if lower_half_pts >= 0:
        good_trips -= select2(lower_half_pts) * pts_at_loc[p1_loc]

    upper_half_pts -= pts_at_loc[p1_loc + 1]
    if p1_loc + half_circ + 1 < c:
        upper_half_pts += pts_at_loc[p1_loc + half_circ + 1]
    if p1_loc + half_circ < c:
        lower_half_pts -= pts_at_loc[p1_loc + half_circ]

print(good_trips, total_trips)