def b_search_index(value, list_sorted:list, leftbound=0, rightbound=-1):
    if rightbound == -1:
        rightbound = len(list_sorted)

    if (rightbound - leftbound == 0):
        return leftbound
    if (rightbound - leftbound == 1):
        if value <= list_sorted[leftbound]:
            return leftbound
        return leftbound + 1
    
    mid = (leftbound + rightbound) // 2
    if value < list_sorted[mid]:
        return b_search_index(value, list_sorted, leftbound=leftbound, rightbound=mid)
    if value > list_sorted[mid]:
        return b_search_index(value, list_sorted, leftbound=mid, rightbound=rightbound)
    return mid

print(b_search_index(1, [1,3,4]))