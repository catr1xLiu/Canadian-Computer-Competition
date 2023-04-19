""" read the inputs"""
c = int(input())  # the number of pairs of triangles

line1, line2 = [], []  # the two lines of triangles
tmp = input().split()
for i in tmp:
    if i == "1":
        line1.append(True)
    else:
        line1.append(False)

tmp = input().split()
for i in tmp:
    if i == "1":
        line2.append(True)
    else:
        line2.append(False)

""" the solution"""
