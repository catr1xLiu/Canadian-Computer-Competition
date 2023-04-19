""" read the inputs"""
c = int(input())  # the number of pairs of triangles

row1, row2 = [], []  # the two rows of triangles
tmp = input().split()
for i in tmp:
    if i == "1":
        row1.append(True)
    else:
        row1.append(False)

tmp = input().split()
for i in tmp:
    if i == "1":
        row2.append(True)
    else:
        row2.append(False)

""" the solution"""
ans = 0
for i in range(c):  # go through all the colums
    if i % 2:  # if the two triangles in the colum are laid top-to-top
        # no mater what, the bottom sides of the two triangles are highlighted whenever they are wet
        ans += row1[i] + row2[i]
        # the left sides of the upper and lower triangles are highlighted whenever they are wet and the sector before(on the left of)  them are dry (else then they are already marked)
        ans += (row1[i] and (not row1[i-1])) + (row2[i] and (not row2[i-1]))
        # the right sides of the upper and lower triangles are highlighted whenever they are wet (we don't need to care about righter triangles because they will be counted later)
        ans += row1[i] + row2[i] 
    
    else:  # if the two triangles in the colum are laid bottom-by-bottom
        #  the side between the upper and lower triangles is highlighted
        ans += row1[i] or row2[i]