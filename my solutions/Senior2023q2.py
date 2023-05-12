
n = int(input())
tmp = input.split()
h=[]
for i in tmp:
    h.append(int(i))
from copy import deepcopy as cp

n = int(input())
tmp = input.split()
h=[]
for i in tmp:
    h.append(int(i))

for length in range(1,n+1):
    for start in range(n-length):
        end = start+length
        tmp = cp(h[start:end])
