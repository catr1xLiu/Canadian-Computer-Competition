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

previously_touched_row = 0
def obsorb_draw_tile():
    hand.append(draw.pop(0))

def print_rows():
    for i in rows:
        print(i)
    print()

while len(draw):
    rows_placed_this_round = []
    flag = False
    if is_double(previously_touched_row):
        for tile_id in range(len(hand)): # go through all tiles in hand
            match = match_tile(hand[tile_id], previously_touched_row)
            if match != -1:
                rows[previously_touched_row].append(match)
                hand.pop(previously_touched_row)
                flag = True

    else:
        for tile_id in range(len(hand)): # go through all tiles in hand
            print(hand[tile_id])
            print(rows_placed_this_round)
            print_rows()

            match = match_tile(hand[tile_id], (previously_touched_row+1)%4)
            if (match != -1) and (previously_touched_row+1 not in rows_placed_this_round):
                rows[previously_touched_row].append(match)
                rows_placed_this_round.append(previously_touched_row)
                hand[previously_touched_row] = -1
                flag = True
            for row in range(4):
                # print(hand,i)
                match = match_tile(hand[tile_id], row)
                if (match != -1) and (row not in rows_placed_this_round):
                    rows[row].append(match)
                    rows_placed_this_round.append(row)
                    hand[tile_id] = -1
                    previously_touched_row = row
                    flag = True

    if not flag:
        obsorb_draw_tile()

print(hand)



''' 
notice, for each pile on our hand, we are asked to examine whether it can be appended to any of the rows, starting with the one AFTER the one to which the last pile is appended to 
'''