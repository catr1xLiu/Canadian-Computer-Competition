import sys
from copy import deepcopy as cp
n = int(input())

orginal, target = list(map(int, input().split())), list(map(int, input().split()))

def get_differences(array):
    differences = []
    for i in range(n):
        if array[i] != target[i]:
            differences.append(i)
        
    return differences

def right(array, start, end):
    ans = cp(array)
    becomes = array[start]
    for i in range(start, end+1):
        ans[i] = becomes
    return ans

def left(array, start, end):
    # print("L", start, end, array)
    ans = cp(array)
    becomes = array[end]
    for i in range(start, end+1):
        ans[i] = becomes
    # print("ans:", ans)
    return ans

def possible(array):
    return set(target).issubset(set(array))


def dfs(array, operations:str):
    # print(array)
    if not possible(array):
        return
    
    flag = True
    for i in range(n):
        if array[i] != target[i]:
            flag = False
            break
    if flag:
        print("YES")
        print((len(operations.splitlines())))
        for i in operations.splitlines():
            if i:
                print(i)
        sys.exit()

    for difference in get_differences(array):
        # print("diff:", difference)
        for i in range(0, difference):
            if target[difference] == array[i]:
                dfs(right(array, i, difference), operations + f"R {i} {difference}\n")
        for i in range(difference+1, n):
            if target[difference] == array[i]:
                dfs(left(array, difference, i), operations + f"L {i} {difference}\n")

dfs(orginal, "")

'''
3
3 1 2
3 1 1
'''

print("NO")