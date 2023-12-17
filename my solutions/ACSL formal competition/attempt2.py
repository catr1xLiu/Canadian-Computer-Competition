rows = []
inp = input()
inp = "0" * (4-len(inp)) + inp 
for i in inp:
    rows.append([int(i)])
tmp = input().split()
hand = []
for i in tmp:
    i = "0" * (2-len(i)) + i 
    hand.append((int(i[0]), int(i[1])))
tmp = input().split()
draw = []
for i in tmp:
    i = "0" * (2-len(i)) + i 
    draw.append((int(i[0]), int(i[1])))

def match_tile(tile, row):
    if tile == -1:
        return -1
    '''
    returns tile, rotated if needed
    '''
    if len(rows[row]) == 1:
        end = rows[row][-1]
    else:
        end = rows[row][-1][1]

    if tile[0] == end:
        return (tile[0], tile[1])
    if tile[1] == end:
        return (tile[1], tile[0])
    return -1

def is_double(row):
    if len(rows[row]) == 1:
        return False
    
    return rows[row][-1][0] == rows[row][-1][1]

previously_touched_row = -1
def obsorb_draw_tile():
    if len(draw) == 0:
        return False
    hand.append(draw.pop(0))
    return True

def print_rows():
    for i in rows:
        print(i)
    print()


while True:
    # print(hand)
    # print(previously_touched_row)
    # print_rows()
    flag = False
    if previously_touched_row != -1 and is_double(previously_touched_row):
        for tile_id in range(len(hand)): # go through all tiles in hand
            match = match_tile(hand[tile_id], previously_touched_row)
            if match != -1:
                rows[previously_touched_row].append(match)
                hand[tile_id] = -1
                flag = True
                break
    else:
        for tile_id in range(len(hand)): # go through all tiles in hand
            if flag:
                break
            match = match_tile(hand[tile_id], (previously_touched_row+1)%4)
            if (match != -1):
                rows[(previously_touched_row+1)%4].append(match)
                hand[tile_id] = -1
                flag=True
                break
            for row in range(4):
                # print(hand,i)
                match = match_tile(hand[tile_id], row)
                if match != -1:
                    rows[row].append(match)
                    hand[tile_id] = -1
                    previously_touched_row = row
                    flag = True
                    break
    if not flag:
        if not obsorb_draw_tile():
            break

sum = 0
for i in hand:
    if i != -1:
        sum += i[0] + i[1]
print(sum)

''' 
notice, for each pile on our hand, we are asked to examine whether it can be appended to any of the rows, starting with the one AFTER the one to which the last pile is appended to 
'''