m = int(input())
n = int(input())

k = int(input())

rows_inversed = [False] * m
colums_inversed = [False] * n

for i in range(k):
    _ = input().split()
    if _[0]== "R":
        rows_inversed[int(_[1])-1] = not rows_inversed[int(_[1])-1]
    else:
        colums_inversed[int(_[1])-1] = not colums_inversed[int(_[1])-1]
        
    
res = 0
for i in rows_inversed:
    for j in colums_inversed:
        res += i!=j 

print(res)