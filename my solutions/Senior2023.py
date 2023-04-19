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
        
        # the left sides of the upper and lower triangles are highlighted whenever they are wet and the sector before(on the left of) them are dry
        ans += (row1[i] and (not row1[i-1])) + (row2[i] and (not row2[i-1]))
        
        # the right sides of the upper and lower triangles are highlighted whenever they are wet and the sector after(on the right of) them are dry (if there are any triangles on the right, in the first place)
        flag = i+1 == c # whether the triangles are the most-righter ones
        ans += (row1[i] and  # the upper triangle is wet and, 
        (flag or (not row1[i+1])))  # its righter neibour is dry or it does not even have a righter neibour
        + (row2[i] and  # the lower triangle is wet and, 
        (flag or (not row2[i+1])))  # its righter neibour is dry or it does not even have a righter neibour
    
    else:  # if the two triangles in the colum are laid bottom-by-bottom
        
        #  the side between the upper and lower triangles is highlighted if one of them is wet (bot not both)
        ans += row1[i] != row2[i]
        
        # the left sides of the upper and lower triangles are highlighted whenever they are wet and the triangles before(on the left of) them are dry (if there are any triangles on the left, in the first place)
        flag = not i # whether the triangles are the most-lefter ones
        ans += (row1[i] and  # the upper triangle is wet and, 
        (flag or (not row1[i-1])))  # its righter neibour is dry or it does not even have a righter neibour
        + (row2[i] and  # the lower triangle is wet and, 
        (flag or (not row2[i-1])))  # its righter neibour is dry or it does not even have a righter neibour
        
        # the right sides of the upper and lower triangles are highlighted whenever they are wet and the sector after(on the right of) them are dry (if there are any triangles on the right, in the first place)
        ans += (row1[i] and  # the upper triangle is wet and, 
        (flag or (not row1[i+1])))  # its righter neibour is dry or it does not even have a righter neibour
        + (row2[i] and  # the lower triangle is wet and, 
        (flag or (not row2[i+1])))  # its righter neibour is dry or it does not even have a righter neibour
        
print(ans)