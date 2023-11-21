# ccc 2022 question 4

n, c = map(int, input().split())
pts_at_loc = [0 for i in range(c)]

for pos in map(int, input().split()):
    pts_at_loc[pos] += 1 

def pt_acc(p):
    return int(p + c/2) + c%2 #can't use round(p+c/2) because python has a stupid logic of round

good_trips = 0
for pt_a in range(int(c/2)):
    if pts_at_loc[pt_a] == 0:
        continue
    pts_inside_good_range = c%2 * pts_at_loc[pt_acc(pt_a)]
    for pt_b in range(pt_a+1, pt_acc(pt_a)):
        good_trips += pts_inside_good_range * pts_at_loc[pt_a] * pts_at_loc[pt_b]
        if pt_acc(pt_b) < c:
            pts_inside_good_range += pts_at_loc[pt_acc(pt_b)]

print(good_trips)