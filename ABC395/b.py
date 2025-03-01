# https://atcoder.jp/contests/abc395/tasks/abc395_b

n = int(input())

grid = []
for _ in range(n):
    grid.append(list("?" * n))


def fill(ofst, color):
    for i in range(ofst, n - ofst):
        for j in range(ofst, n - ofst):
            grid[i][j] = color


for i in range(n):
    j = n - i + 1
    if i > j:
        continue
    if i % 2 == 0:
        fill(i, "#")
    else:
        fill(i, ".")

for row in grid:
    for col in row:
        print(col, end="")
    print()
