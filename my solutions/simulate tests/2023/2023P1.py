c = int(input())
_ = input().split()
upper_colum = []
for i in _:
    upper_colum.append(int(i))

_ = input().split()
lower_colum = []
for i in _:
    lower_colum.append(int(i))

total_tapes = (sum(upper_colum) + sum(lower_colum)) * 3  # the total amount of tap used for surround every single painted triangles

for i in range(c):
    # left and right neighbours
    if i > 0 and upper_colum[i] == 1 == upper_colum[i-1]:
        total_tapes -= 2 # not needed for the left side
    if i > 0 and lower_colum[i] == 1 == lower_colum[i-1]:
        total_tapes -= 2

    # up and down
    if i % 2 == 0 and upper_colum[i] == lower_colum[i] == 1:
        total_tapes -= 2

print(total_tapes)
