import sys

n, m, r, c = map(int, input().split())

def printlines(lines):
    for i in lines:
        for j in i:
            print(j, end=" ")
        print()

if r == n and m == c:
    print(("a"*m + "\n") * n, end="")
    sys.exit()
elif r == n: 
    # when all rows are palindromic, it mesns thst the shape is horizontally symetric
    if c%2 == 1:
        # so, it is impossible to have odd number of asymetric 
        print("IMPOSSIBLE")
        sys.exit()
        
    # first, make the matrix like this, so thwt all rows are symettic  and all colums asymetric
    '''
    a a a a 
    b b b b 
    b b b b 
    b b b b
    '''
    lines = [['a' for i in range(m)]] + [['b' for i in range(m)] for j in range(n-1)]
    for i in range(c/2):
        lines[0][i] = lines[0][-1-i] = 'b'
    printlines(lines)
    sys.exit()
elif m == c:
    if r%2:
        print("IMPOSSIBLE")
        sys.exit()
    '''
    a b b b 
    a b b b 
    a b b b 
    '''
    lines = [
        (['a']+[b for i in range(m-1)])
        for j in range(n)]
    for i in range(r/2):
        lines[i][0] = lines[-1-i][0] = 'c'
    printlines(lines)
    sys.exit()

 # initialize the matrix with this patteren, so that all rows and colums are not palindromic
'''
 a b b b b
 b a a a a
 b a a a a
 b a a a a
'''
lines = [['a'] + ['b' for i in range(m-1)]]
for i in range(n-1):
    lines.append(['b'] + ['a' for i in range(m-1)])

# make r rows symetric by turing the first letter of these rows into a
for i in range(c):
    lines[0][i+1] = 'a'
if r == n-1:
    lines[0][0]='c' # avoid turning the first line symetric again

for i in range(r):
    lines[i+1][0] ='a'
if c == m-1:
    lines[0][0] = 'c'

printlines(lines)