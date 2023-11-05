n, c = map(int, input().split())
pts_at_loc = [0 for i in range(c)]

for pos in map(int, input().split()):
    pts_at_loc[pos] += 1 

def pt_acc(p):
    return int(p + c/2) + c%2 #can't use round(p+c/2) because python has a stupid logic of round
    
'''
思路转变，算出总共有多少个Triplets不是好的，然后用总数减去它
第一个点为i的三角，有
'''