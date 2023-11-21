'''
虽然坏三角不一定在数字最小的那一个点的直径一侧，但一定在某一条直径的一侧。如果我们把一个坏三角最靠顺时针方向的点叫p1，那么我们可以顺着逆时针，在p1点连成的直径一侧任选p1和p3，还不会选重复
'''

n, c = map(int, input().split())
pts_at_loc = [0 for i in range(c)]

for pos in map(int, input().split()):
    pts_at_loc[pos] += 1 

half_circ = int(c/2) # half of the circle
def pt_acc(p):
    return (p + half_circ +1)%c 

def select2(n): 
    # select 2 random pts from n points, orders don't matter
    return (n-1) * n / 2 # (n-1) + (n-2) + ... + 1

total_trips = 0
pts_inside_range = sum(pts_at_loc)
for i in range(c-2):
    pts_inside_range -= pts_at_loc[i]
    total_trips += select2(pts_inside_range) * pts_at_loc[i]
print(total_trips)

pts_inside_counter_range=sum(pts_at_loc[0:half_circ+1])

good_trips = total_trips
for p1 in range(c):
    pts_inside_counter_range -= pts_at_loc[p1]
    good_trips -= select2(pts_inside_counter_range) * pts_at_loc[p1]
    print(p1,pts_inside_counter_range, select2(pts_inside_counter_range) * pts_at_loc[p1])
    pts_inside_counter_range += pts_at_loc[pt_acc(p1)]

print(good_trips)