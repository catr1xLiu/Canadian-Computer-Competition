m, n = int(input()), int(input())

room = []
for i in range(m):
    room.append(list(map(int, input().split())))

cells_by_number = {}
for x in range(m):
    for y in range(n):
        num = room[x][y]
        if num in cells_by_number:
            cells_by_number[num].append((x,y))
        else:
            cells_by_number[num] = [(x,y)]

tocuhed_cells = set() # [(x, y), (x,y)... where 0<x<m and 0<y<n], starting from (m,n)
tocuhed_cells.add((m-1, n-1))
cells_to_be_examined = set()
cells_to_be_examined.add((m-1, n-1))
numbers_examined = set()
while True:
    to_be_added_cells = []
    for cell_to_be_examined in cells_to_be_examined:
        num = (cell_to_be_examined[0]+1) * (cell_to_be_examined[1]+1)
        if num in cells_by_number and num not in numbers_examined:
            for cell in cells_by_number[num]:
                if cell not in tocuhed_cells:
                    to_be_added_cells.append(cell)
        numbers_examined.add(num)
    cells_to_be_examined = set()
    for to_be_added_cell in to_be_added_cells:
        tocuhed_cells.add(to_be_added_cell)
        cells_to_be_examined.add(to_be_added_cell)
    if (not to_be_added_cells) or (0, 0) in tocuhed_cells:
        break

if (0, 0) in tocuhed_cells:
    print("yes")
else:
    print("no")

'''
3
4
3 10 8 14
1 11 12 12
6 2 3 9
'''