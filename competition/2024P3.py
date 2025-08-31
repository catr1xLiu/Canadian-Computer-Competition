n = int(input())

orginal, target = list(map(int, input().split())), list(map(int, input().split()))

differences = [] # [(start_at, end_before)]

current_difference = [0,0]
for i in range(n):
    if orginal[i] == target[i]:
        if current_difference[0] != current_difference[1]:
            differences.append(tuple(current_difference))
        current_difference[0] = current_difference[1] = i+1
    else:
        current_difference[1] += 1
if current_difference[0] != current_difference[1]:
    differences.append(tuple(current_difference))

operations = []
flag = True
for difference in differences:
    if difference[0] <= 0:
        if difference[1]>= n:
            flag = False
            break
        right_neibour = orginal[difference[1]]
        for i in range(difference[0], difference[1]):
            if target[i] != right_neibour:
                flag = False
                break
        operations.append(f"L {difference[0]} {difference[1]}")
        continue
    elif difference[1]>= n:
        left_neibour = orginal[difference[0]-1]
        for i in range(difference[0], difference[1]):
            if target[i] != left_neibour:
                flag = False
                break
        operations.append(f"R {difference[0]-1} {difference[1]-1}")
        continue
    if not flag:
        break

    right_neibour = orginal[difference[1]]
    left_neibour = orginal[difference[0]-1]
    pending_right_starting_from = None
    for i in range(difference[0], difference[1]):
        if pending_right_starting_from is None: # pending left
            if left_neibour == target[i]:
                continue
            if difference[0] != i:
                operations.append(f"R {difference[0]-1} {i-1}")
            pending_right_starting_from = i
        else:
            if right_neibour != target[i]:
                flag = False
                break
    if pending_right_starting_from is not None:
        operations.append(f"L {pending_right_starting_from} {difference[1]}")

    if not flag:
        break

if flag:
    print("YES")
    print(len(operations))
    for i in operations:
        print(i)
    
else:
    print("NO")

'''
6   
0 1 2 3 4 5
0 1 2 5 5 5

6
0 1 2 3 4 5
0 1 1 1 5 5
'''