def b_search_index(value, indexes_sorted:list, values:dict, left_bound=0, rightbound=-1):
    if rightbound == -1:
        rightbound = len(indexes_sorted)

    if (rightbound - left_bound == 2):
        return left_bound + 1
    if (rightbound - left_bound == 1):
        if value < values[indexes_sorted[left_bound]]:
            return left_bound-1
        return left_bound + 1
    
    mid = (left_bound + rightbound) // 2
    if value < values[indexes_sorted[mid]]:
        return b_search_index(value, indexes_sorted, values, left_bound=left_bound, rightbound=mid)
    return b_search_index(value, indexes_sorted, values, left_bound=mid, rightbound=rightbound)


values = dict()
values[0] = 0
values[1] = 1
values[2] = 2
values[3] = 3
values[4] = 4

print(b_search_index(3.5, [0,1,2,3,4], values))