n = int(input())

def b_search(l, x, mi=0, ma=-1): # inclusive
    if ma == -1:
        ma = len(l)-1
    if len(l) < 5:
        for i in range(mi, ma+1):
            if l[i] == x:
                return (i, i)
            if l[i-1] < x and l[i] > x:
                return (i-1, i)
        return -1
    guess = int((ma-mi)/2)
    if l[guess] < x:
        return b_search(l, x, guess, ma)
    else if l[guess] > x:
        return b_search(l, x, mi, guess)
    else:
        return (guess, guess)
            
friends = []
max_p = 0
for i in range(n):
    p, w, d = map(int, input().split())
    friends.append((p, w, d))
    max_p = max(max_p, p)
    
segment_pts_x = []
segment_pts_y = []

def linear_interp(pt1, pt2, x):
    k = (pt2[1]- pt1[1]) / (pt2[0] - pt1[0])
    return pt1[1] + (x-pt1[0]) * k
    
def inset_pt(x):
    loc = b_search(segment_pts_x, x)
    if loc[0] == loc[1]:
        return
    if loc==-1:
        segment_pts_x.append((x,0))
        return 
    y = linear_interp((segment_pts_x[loc[0]],segment_pts_y[loc[0]]),  (segment_pts_x[loc[1]], segment_pts_y[loc[1]]), x)
    segment_pts_x.insert(loc[1], x)
    segment_pts_y.insert(loc[1], y)
    
for friend in friends:
    newpts = []
    if p-d >= 0:
        newpts.append([0, i[w] * i[p-d]])
    newpts.append([max(0,p-d), 0])
    newpts.