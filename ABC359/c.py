sx, sy = list(map(int, input().split()))
tx, ty = list(map(int, input().split()))

hori = abs(sx - tx)
vert = abs(sy - ty)

if vert >= hori:
    print(vert)
    exit()

# ignorable = 0
# if sy % 2 == 0 and sx % 2 != 0 and sx - tx > 0:  # move to left
#     ignorable += 1
# elif sy % 2 == 0 and sx % 2 == 0 and sx - tx < 0:  # move to right
#     ignorable += 1
# elif sy % 2 != 0 and sx % 2 != 0 and sx - tx < 0:  # move to right
#     ignorable += 1
# elif sy % 2 != 0 and sx % 2 == 0 and sx - tx > 0:  # move to left
#     ignorable += 1
# print(vert + 1 + ignorable)
print(vert + 1)
print((hori - vert) // 2)
