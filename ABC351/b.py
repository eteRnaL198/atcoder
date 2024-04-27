n = int(input())

grid_a = []
for i in range(n):
    grid_a.append(input())

grid_b = []
for i in range(n):
    grid_b.append(input())

for i in range(n):
    for j in range(n):
        if grid_a[i][j] != grid_b[i][j]:
            print(i + 1, j + 1)
