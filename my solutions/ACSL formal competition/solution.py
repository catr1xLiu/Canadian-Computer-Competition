'''
5923
56 27 73 34 99 45 32 17 64 57 18 11
36 92 22 50 82

1324
85 31 32 96 25 1 68
30 35 42 11 78 39 19 9 81
'''
rows = []


inp = input()
inp = "0" * (4-len(inp)) + inp 
for i in inp:
    rows.append([int(i)])

tmp = input().split()
hand = []
for i in tmp:
    hand.append((int(i[0]), int(i[1])))
tmp = input().split()
draw = []
for i in tmp:
    draw.append((int(i[0]), int(i[1])))

start_searching_pos = last_touched_row = 0

def match_element_to_row(elements, element_id, row):
    if elements[element_id] == -1:
        return False
    global last_touched_row
    '''
    returns: successful or not
    '''
    if (len(rows[row]) == 1):
        end = rows[row][-1]
    else:
        end = rows[row][-1][1] # the last one

    if elements[element_id][0] == end:
        rst = (elements[element_id][0], elements[element_id][1])
        rows[row].append(rst)
        last_touched_row = row
        elements[element_id] = -1
        return True
    if elements[element_id][1] == end:
        rst = (elements[element_id][1], elements[element_id][0])
        rows[row].append(rst)
        last_touched_row = row
        elements[element_id] = -1
        return True
    return False

def match_element_to_rows(element_id):
    '''
    return successful or not
    '''
    if match_element_to_row(hand, element_id, start_searching_pos):
        return True

    for i in range(4):
        if match_element_to_row(hand, element_id, i):
            return True

    return False


while len(draw):
    start_searching_pos = last_touched_row
    elements_to_pop_ids = []
    for i in rows:
        print(i)
    print(start_searching_pos)

    double_pos = -1
    for i in range(len(rows)):
        if len(rows[i]) == 1:
            continue
        if rows[i][-1][0] == rows[i][-1][1]:
            double_pos = i

    print(double_pos)
    print()
    # print(hand, "\n", draw, "\n")
    if (double_pos == -1):
        flag = False
        for i in range(len(hand)):
            flag = flag or match_element_to_rows(i)
        if flag:
            continue
    else:
        flag = False
        for i in range(len(hand)):
            if match_element_to_row(hand, i, double_pos):
                flag = True
                break
        if flag:
            continue
    # here, if no match is found, pull from draw
    hand.append(draw.pop(0))

print(hand)
sum = 0
for i in hand:
    if i == -1:
        continue
    sum += i[0] + i[1]

print(sum)