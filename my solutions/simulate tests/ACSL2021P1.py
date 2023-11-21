def to_hex(x):
    x = str(x)
    ans = p = 0
    for i in range(len(x)-1, -1, -1):
        ans += int(x[i]) * 8**p
        p += 1
    return ans
    
def to_oct(x):
    ans = ""
    while x!=0:
        ans = str(x%8) + ans 
        x = int(x/8)
    return ans

def su(x):
    ans = 0
    for i in str(x):
        ans += int(i)
    return ans    

for i in range(5):
    ans = 0
    s, d, r = map(int, input().split())
    d = to_hex(d)
    s = to_hex(s)
    s += (r)*(r-1)/2 * d
    for i in range(r):
        ans += su(to_oct(int(s)))
        s += d
    print(ans)