from copy import deepcopy as cp

n = int(input())
tmp = input.split()
h=[]
for i in tmp:
    h.append(int(i))

    
def find_asymmetric_value(heights):
    length = len(heights)
    asymmetric = 0
    for i in range(int(length/2)):
        asymmetric += abs(heights[i] - heights[-1-i])
    return asymmetric
    
for length in range(1,n+1):
    min_asymmetric = float("inf")
    for start in range(n-length):
        end = start+length
        h1 = cp(h[start:end])
        min_asymmetric = min(find_asymmetric(h1), min_asymmetric)
    print(min_asymmetric,end=" ")
