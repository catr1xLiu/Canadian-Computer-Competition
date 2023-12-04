n = int(input())

friends = [] #(p, w, d)
max_p = 0
total_w = 0
total_t = 0

key_pts = {} # {position: increase in k}
key_pts_pos = []
for i in range(n):
    p, w, d = map(int, input().split())
    friends.append((p, w, d))
    max_p = max(max_p, p)
    if p-d >= 0:
        total_w -= w
        total_t += w*(p-d)
        try:
            key_pts[p-d] += w
        except KeyError:
            key_pts[p-d] = w
        key_pts_pos.append(p-d)

    try:
        key_pts[p+d] += w
    except KeyError:
        key_pts[p+d] = w
    key_pts_pos.append(p+d)

result = total_t
previous_position = 0
key_pts_pos.sort()
for i in key_pts_pos:
    position = i
    total_t += total_w * (position-previous_position)
    total_w += key_pts[i]
    result = min(result, total_t)
    previous_position = position
    print(i, total_t, total_w)
    
print(result)