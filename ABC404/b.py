# https://atcoder.jp/contests/abc404/tasks/abc404_b


from copy import deepcopy

n = int(input())
s_nn = [list(input()) for _ in range(n)]
t_nn = [list(input()) for _ in range(n)]


def rotate(grid):
    rotated = deepcopy(grid)
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = grid[i][j]
    return rotated


def change_count(grid, num):
    for x in range(n):
        for y in range(n):
            if grid[x][y] != t_nn[x][y]:
                num += 1
    return num


var1 = s_nn
num1 = 0
answer1 = change_count(var1, num1)
var2 = rotate(s_nn)
num2 = 1
answer2 = change_count(var2, num2)
var3 = rotate(var2)
num3 = 2
answer3 = change_count(var3, num3)
var4 = rotate(var3)
num4 = 3
answer4 = change_count(var4, num4)

print(min(answer1, answer2, answer3, answer4))
