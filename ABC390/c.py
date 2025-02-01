# https://atcoder.jp/contests/abc390/tasks/abc390_c


h, w = list(map(int, input().split()))
grid = []
for i in range(h):
    grid.append(list(input()))

top = h + 1
right = -1
bottom = -1
left = w + 1
for i in range(h):
    for j in range(w):
        if grid[i][j] != "#":
            continue
        if i < top:
            top = i
        if j > right:
            right = j
        if i > bottom:
            bottom = i
        if j < left:
            left = j


for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if grid[i][j] == ".":
            print("No")
            exit()
print("Yes")
